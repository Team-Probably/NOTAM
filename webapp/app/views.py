# views.py
from flask import render_template, request, Response, redirect, url_for, session, jsonify
import json
import os
import datetime
from app import app
from app import extract
from app import database
from werkzeug.datastructures import ImmutableMultiDict
from pprint import pprint
from datetime import datetime
import random
import smtplib
import ssl

#import overpy
# app.secret_key = "WORKS"
app.secret_key = os.environ['FLASK_SECRET_KEY']


# URL Routes
# @app.route('/')
# def index():
#     print("INDEX")
#     session['username'] = {}
#     return render_template("login.html")

@app.route('/')
@app.route('/dashboard')
def dashboard():
    airspace = database.get_notams('airspace')
    facility = database.get_notams('facility')
    print(airspace, facility)
    for i in range(len(airspace)):
        airspace[i]['msg'] = airspace[i]['msg'].replace('\n', '<br/>')
    for i in range(len(facility)):
        facility[i]['msg'] = facility[i]['msg'].replace('\n', '<br/>')
    print(airspace, facility)
    if session.get('verification_code'):
        vcs = True
    else:
        vcs = False

    return render_template("dashboard_v2/newdash.html", facility=facility, airspace=airspace, logged_in=check_login(), vcs=vcs)


@app.route('/admin_airspace')
def admin_airspace():
    try:
        if session['username']['admin'] != True:
            return redirect(url_for('dashboard'))
    except:
        return redirect(url_for('dashboard'))
    else:
        notam = {'class': 'Notam Series', 'airport': '', 'notam': '', 'start_date': 'Start Date',
                 'end_date': 'End Date', 'start_time': 'Start Time', 'end_time': 'End Time',
                 'notam_no': ''}
        return render_template("dashboard_v2/index.html", notam=notam)


@app.route('/admin_facility')
def admin_facility():
    try:
        if session['username']['admin'] != True:
            return redirect(url_for('dashboard'))
    except:
        return redirect(url_for('dashboard'))
    else:
        notam = {'class': 'Notam Series', 'airport': '', 'notam': '', 'start_date': 'Start Date',
                 'end_date': 'End Date', 'start_time': 'Start Time', 'end_time': 'End Time',
                 'notam_no': ''}
    return render_template("dashboard_v2/Facility.html", notam=notam)


# Request Routes
@app.route('/processor', methods=['POST'])
def processor():

    return Response(
        json.dumps(
            extract.extract('NOTAM.pdf')
        ), mimetype='application/json'
    )


@app.route('/create_notam', methods=['POST'])
def create():
    notam = {}
    data = request.get_json()
    print(data)
    if data['notam_type'] == 'airspace':
        keys = ['notam_notam', 'notam_series', 'notam_no', 'fir', 'scenario', 'nature',
                'latin', 'longin', 'stime', 'etime', 'remarks', 'map_poly', 'zoom', 'llimit', 'ulimit', 'notam_type']
    else:
        keys = ['notam_series', 'notam_no', 'fir', 'ident', 'freq', 'latin', 'longin', 'stime', 'etime',
                'remarks', 'map_poly', 'zoom', 'notam_type']
    notam_data = ""
    if data.get('notam_notam'):
        data['msg'] = data['notam_notam']
    else:
        msg = ''
        msg += data['notam_series']+data['notam_no']+'/'+'19'+' NOTAMN\n'
        msg += 'Q) '+data['fir']+'\n'
        msg += 'A) '+data['fir']+' B) '+data['stime'].replace('/', '').replace(' ', '').replace(
            ':', '')+' C) '+data['etime'].replace('/', '').replace(' ', '').replace(':', '')+'\n'
        try:
            coords = 'AROUND ' + \
                str(round(float(data['latin'])*10000, 2))+'N' + \
                ' '+str(round(float(data['longin'])*10000, 2))
        except:
            try:
                coords = 'WITHIN THE REGION '
                if data['map_poly'][0]:
                    coords += "CENTERED AT "+str(0.000539957*data['map_poly'][0][0]) + " " + str(
                        0.000539957*data['map_poly'][0][0]) + " RADIUS " + str(0.000539957*data['map_poly'][1])
                coords += '\n'
                for i in data['map_poly'][2][0]:
                    coords += 'lat : ' + \
                        str(i['lat']) + " lng : " + str(i['lng'])+"\n"
            except:
                coords = ''
        msg += 'E) '+(' AIRSPACE ' if data['notam_type'] == 'airspace' else 'FACILITY ')+data.get(
            'scenario', '')+' DUE '+data.get('nature', '')+' '+coords+'\n'
        msg += data.get('remarks', '')+'\n '
        nw = datetime.utcnow()
        msg += 'Created On: '+str(nw.year)+'/'+str(nw.month) + \
            '/'+str(nw.day)+' '+str(nw.hour)+':'+str(nw.minute)
        data['msg'] = msg
    keys.append('msg')
    for key in keys:
        notam[key] = data[key]
        # notam_data += " " + notam[key]
    notam['coords'] = []
    notam['coords'].append((notam['latin'], notam['longin']))
    # notam_extract = extract.extract_is_back(notam_data['notam_notam'])
    notam['issued_by'] = "Administrator"

    # for key in notam_extract.keys():
    #     notam[key] = notam_extract[key]
    print(notam)
    if database.add_notam(notam):
        return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}
    else:
        return json.dumps({'success': "NOTAM Exists"}), 200, {'ContentType': 'application/json'}


@app.route('/signup', methods=['POST'])
def signup():
    user = request.form
    user = user.to_dict(flat=False)
    for key in user.keys():
        user[key] = user[key][0]
    if user['secretKey'] == os.environ['secretKey']:
        user['admin'] = True
    else:
        user['admin'] = False
    if database.add_user(user):
        return redirect(url_for('dashboard'))
    return redirect(url_for('dashboard'))


@app.route('/sign_up')
def sign_up():
    return render_template("login.html")


@app.route('/verify_login', methods=['POST'])
def verify_login():
    user = request.form
    user = user.to_dict(flat=False)
    print('verificode' in user)
    print(user)
    #print(session.get('verification_code'), user['verificode'])
    if 'verificode' in user and session.get('verification_code'):
        if user['verificode'][0] == session['verification_code']:
            print("LOGIN SUCCESSFUL")
            session['username'] = session['username_temp']
            session.pop('verification_code', None)
            print(session['username'])
        return redirect(url_for('dashboard'))
    else:
        for key in user.keys():
            user[key] = user[key][0]
        user = database.verify_login(user)
        print(user)
        if user:
            vcode = ''
            for i in range(6):
                vcode += str(random.randint(0, 9))
            session['verification_code'] = vcode
            sendemail(user['email'], vcode)
            session['username_temp'] = {
                'user_name': user['email'], 'admin': user['admin'], "key": app.secret_key}
        return redirect(url_for('dashboard'))


def sendemail(rec, vc):

    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "teamprobably@gmail.com"  # Enter your address
    receiver_email = rec  # Enter receiver address
    password = os.environ['TPPASS']
    message = """\
    Subject: Hi there

    Here's your OTP! """+vc
    print(message)
    context = ssl.create_default_context()
    try:
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)
    except:
        pass


@app.route('/getnotamdata')
def getnotamdata():
    notam_no = request.args.get('notamid')
    notam = database.get_notam('notam_no', notam_no)
    notam['_id'] = 'hi'
    return jsonify(notam)


@app.route('/editnotam', methods=['POST'])
def edit_notam():
    notam_no = request.args.get('notamid')
    notam = database.get_notam('notam_no', notam_no)
    notam['_id'] = 'hi'
    return jsonify(notam)


@app.route('/deletenotam')
def deletenotam():
    notam_no = request.args.get('notamid')
    result = database.remove_notam('notam_no', notam_no)
    return result


@app.route('/predict_notam', methods=["GET"])
def predict_notam():
    notam = request.args.get('notam')
    notam = extract.extract_is_back(notam)
    print(notam)
    notam['start_date'], notam["start_time"] = notam['starttime'].split(" ")
    notam['end_date'], notam["end_time"] = notam['endtime'].split(" ")
    if notam['firOfac'] == 'FIR':
        return render_template('dashboard_v2/Facility.html', notam=notam)
    else:
        return render_template('dashboard_v2/index.html', notam=notam)


def check_login():
    #print(request, type(request))
    try:
        if(session['username']['admin'] == True):
            return True
        else:
            return False
    except:
        return False


def overpass_aerodrome(query):
    pass


def overpass_runway(query):
    pass


def overpass_taxiway(coords):
    api = overpy.Overpass()
    q = """
    way({}) ["aeroway"="taxiway"];
    (._;>;);
    out body;
    """.format(str(coord))
    result = api.query()
    res = {}
    for way in result.ways:
        print("Name: %s" % way.tags.get("name", "n/a"))
        print("Highway: %s" % way.tags.get("taxiway", "n/a"))
        print("Nodes:")
        nod = []
        for node in way.nodes:
            print("Lat: %f,Lon: %f" % (node.lat, node.lon))
            nod.append([node.lat, node.lon])
        res[way.tags.get("name", "n/a")] = nod
    return res


@app.route('/logout')
def logout():
    session['username'] = None
    return redirect(url_for('dashboard'))

# DEBUG URLs
@app.route('/visualizer')
def visualizer():
    return render_template("visualizer/visual.html")


@app.route('/populate')
def populate_notams():
    database.populate()
    return redirect(url_for('dashboard'))


@app.route('/listview')
def listview():
    return render_template("index.html")


@app.route('/admin1')
def admin1():
    try:
        if session['username']['admin'] != True:
            return redirect(url_for('index'))
    except:
        return redirect(url_for('index'))
    airspace = database.get_notams('airspace')
    facility = database.get_notams('facility')
    return render_template('admin.html', facility=facility, airspace=airspace)


@app.route('/dashboard2')
def dashboard2():
    airspace = database.get_notams('airspace')
    facility = database.get_notams('facility')
    print(airspace, facility)
    return render_template("dashboard.html", facility=facility, airspace=airspace)


@app.route('/kittu')
def kittu():
    return render_template("kittu.html")


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


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
