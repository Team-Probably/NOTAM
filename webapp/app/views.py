# views.py
from flask import render_template,request,Response,redirect,url_for,session,jsonify
import json,os,datetime
from app import app
from app import extract
from app import database
from werkzeug.datastructures import ImmutableMultiDict
from pprint import pprint
from datetime import datetime

app.secret_key = os.environ['FLASK_SECRET_KEY']

@app.route('/') #TO-DO : By Aditya and Avi 
def index():
    print("INDEX")
    session['username'] = {}
    return render_template("login.html")    


@app.route('/visualizer') #TO-DO : By Kiteretsu
def visualizer():
    return render_template("visualizer/visual.html")


@app.route('/listview') 
def listview():
    return render_template("index.html")

@app.route('/admin1')
def admin():
    try:
        if session['username']['admin']!=True:
            return redirect(url_for('index'))
    except:
        return redirect(url_for('index'))
    airspace = database.get_notams('airspace')
    facility = database.get_notams('facility')
    
    return render_template('admin.html', facility=facility, airspace=airspace)


@app.route('/processor', methods=['POST'])  # TO-DO : By Rushang and akshay
def processor():

    return Response(
            json.dumps(
                    extract.extract('NOTAM.pdf')
                ), mimetype='application/json'
            )

@app.route('/dashboard') #USER : Notam Lists
def dashboard():
    airspace = database.get_notams('airspace')
    facility = database.get_notams('facility')
    print(airspace, facility)
    return render_template("dashboard.html", facility = facility , airspace = airspace)

@app.route('/create_notam',methods=['POST']) #Admin : Create Notams
def create():
    notam = {}
    data = request.get_json()
    print(data)
    if data['notam_type'] == 'airspace':
        keys = ['notam_notam', 'notam_series', 'notam_no', 'fir', 'scenario', 'nature', 
                'latin', 'longin', 'stime', 'etime', 'remarks', 'map_poly', 'zoom', 'llimit', 'ulimit','notam_type']
    else:
        keys = ['notam_series', 'notam_no', 'fir', 'ident', 'freq', 'latin', 'longin', 'stime', 'etime',
        'remarks','notam_type']    
    notam_data = ""
    print(data)
    if data.get('notam_notam'):
        data['msg']=data['notam_notam']
    else:
        msg = ''
        msg+=data['notam_series']+data['notam_no']+'/'+'19'+' NOTAMN\n'
        msg += 'Q) '+data['fir']+'\n'
        msg+='A) '+data['fir']+' B) '+data['stime'].replace('/', '').replace(' ', '').replace(':', '')+' C) '+data['etime'].replace('/', '').replace(' ', '').replace(':', '')+'\n'
        try:
            coords = 'AROUND '+str(round(float(data['latin'])*10000, 2))+'N'+' '+str(round(float(data['longin'])*10000, 2))
        except:
            try:
                coords = 'WITHIN THE REGION '+str(data['map_poly'])
            except:
                coords = ''
        msg+='E) '+(' AIRSPACE ' if data['notam_type']=='airspace' else 'FACILITY ')+data.get('scenario', '')+' DUE '+data.get('nature', '')+' '+coords+'\n'
        msg+=data.get('remarks', '')+'\n '
        nw = datetime.utcnow()
        msg+='Created On: '+nw.year+'/'+nw.month+'/'+nw.day+' '+nw.hour+':'+nw.minute
        data['msg']=msg
    keys.append('msg')
    for key in keys:
        notam[key] = data[key]
        # notam_data += " " + notam[key]
    # notam status
    
    notam['coords'] = []
    notam['coords'].append((notam['latin'],notam['longin']))
    # notam_extract = extract.extract_is_back(notam_data['notam_notam'])
    notam['issued_by'] = "Administrator"

    # for key in notam_extract.keys():
    #     notam[key] = notam_extract[key]
    print(notam)
    if database.add_notam(notam):
        return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}
    else:
        return json.dumps({'success': "NOTAM Exists"}), 200, {'ContentType': 'application/json'}

@app.route('/signup',methods=['POST']) #User : Login
def signup():
    user = request.form
    user = user.to_dict(flat=False)
    for key in user.keys():
        user[key] = user[key][0]   
    user['admin'] = False
    if database.add_user(user):
        return redirect(url_for('dashboard'))
    return redirect(url_for('index'))

@app.route('/verify_login',methods=['POST']) #User : SignUp
def verify_login():
    user = request.form
    user = user.to_dict(flat=False)
    for key in user.keys():
        user[key] = user[key][0]
    user = database.verify_login(user)
    print(user)
    if user:
        print("LOGIN SUCCESSFUL")
        session['username'] = {'user_name':user['email'],'admin':user['admin'], "key":app.secret_key} 
        print(session['username'])
        return redirect(url_for('dashboard'))
    return redirect(url_for('index'))

@app.route('/getnotamdata')
def getnotamdata():
    notam_no = request.args.get('notamid')
    notam = database.get_notam('notam_no',notam_no)
    notam['_id']='hi'
    return jsonify(notam)

@app.route('/deletenotam')
def deletenotam():
    notam_no = request.args.get('notamid')
    result = database.remove_notam('notam_no',notam_no)
    return result

@app.route('/test')
def test():
    tnot = '''A0422/19 NOTAMN
Q) VOMF/QWALW/IV/NBO/W/000/140/
A) VOMF B) 1902270305 C) 1903040510
D) FEB 27 28, MAR 01 02 AND 04 BTN 0305-0510
E) AIRSPACE BOUNDED BY COORD 103456N 0763816E - 105113N 0765726E
THEN ALONG CLOCKWISE ARC OF 15NM RADIUS CENTRED AT SULUR ARP TILL
110959N 0772134E - 112528N 0774130E THEN ALONG CLOCKWISE ARC OF 40NM
RADIUS CENTRED AT SULUR ARP TILL 103456N 0763816E IS RESERVED FOR
FLYPAST AND AIR DISPLAY AT IAF STATION SULUR FOR PRESIDENTS STANDARD
PRESENTATION. AS A CONSEQUENCE OF AIRSPACE CLOSURE COIMBATORE AP
WILL REMAIN CLSD FOR ACFT OPS.
F) GND G) FL140'''
    return str(extract.extract_is_back(tnot))

@app.route('/kittu')  # USER : Notam Lists
def kittu():
    return render_template("kittu.html")



@app.route('/dashboard2')
def dash2n():
    airspace = database.get_notams('airspace')
    facility = database.get_notams('facility')
    for notam in airspace:
        # notam status
        dtls = list(map(int,notam['stime'].split(' ')[0].split('/')+notam['stime'].split(' ')[1].split(':')))
        dtle = list(map(int,notam['etime'].split(' ')[0].split('/')+notam['etime'].split(' ')[1].split(':')))
        st = datetime(dtls[0], dtls[1], dtls[2], dtls[3], dtls[4])
        et = datetime(dtle[0], dtle[1], dtle[2], dtle[3], dtle[4])
        now = datetime.utcnow()
        if st>now:
            notam['status'] = "Upcoming"
        elif et<now:
            notam['status'] = "Expired"
        else:
            notam['status'] = "Ongoing"
        print(notam)
    for notam in facility:
        # notam status
        dtls = list(map(int,notam['stime'].split(' ')[0].split('/')+notam['stime'].split(' ')[1].split(':')))
        dtle = list(map(int,notam['etime'].split(' ')[0].split('/')+notam['etime'].split(' ')[1].split(':')))
        st = datetime(dtls[0], dtls[1], dtls[2], dtls[3], dtls[4])
        et = datetime(dtle[0], dtle[1], dtle[2], dtle[3], dtle[4])
        now = datetime.utcnow()
        if st>now:
            notam['status'] = "Upcoming"
        elif et<now:
            notam['status'] = "Expired"
        else:
            notam['status'] = "Ongoing"
        
    return render_template("dashboard_v2/newdash.html", facility = facility , airspace = airspace)


@app.route('/admin')  # USER : Notam Lists
def dash2():
    notam = {'class': 'Notam Series', 'airport': '', 'notam': '', 'start_date': 'Start Date',
             'end_date': 'End Date', 'start_time': 'Start Time', 'end_time': 'End Time',
             'notam_no': ''}
    try:
        if session['username']['admin']!=True:
            return redirect(url_for('index'))
    except:
        return redirect(url_for('index'))
    else:
        return render_template("dashboard_v2/index.html", notam=notam)

@app.route('/admin3')  # USER : Notam Lists
def dash3():
    notam = {'class': 'Notam Series', 'airport': '', 'notam': '', 'start_date': 'Start Date',
     'end_date': 'End Date', 'start_time': 'Start Time', 'end_time': 'End Time',
      'notam_no':''}
    return render_template("dashboard_v2/Facility.html",notam=notam)

@app.route('/predict_notam', methods=["GET"])
def predict_notam():
    notam = request.args.get('notam')
    notam = extract.extract_is_back(notam)
    notam['start_date'],notam["start_time"] = notam['starttime'].split(" ")
    notam['end_date'], notam["end_time"] = notam['endtime'].split(" ")
    print(notam)
    if notam['firOfac'] == 'FIR':
        return render_template('dashboard_v2/Facility.html', notam=notam)
    else:
        return render_template('dashboard_v2/index.html', notam=notam)
