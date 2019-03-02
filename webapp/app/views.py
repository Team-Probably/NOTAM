# views.py
from flask import render_template,request,Response,redirect,url_for,session
import json,os,datetime
from app import app
from app import extract
from app import database
from werkzeug.datastructures import ImmutableMultiDict

app.secret_key = os.environ['FLASK_SECRET_KEY']
app.username = ""

@app.route('/') #TO-DO : By Aditya and Avi 
def index():
    session['username'] = ""
    return render_template("login.html")    


@app.route('/visualizer') #TO-DO : By Kiteretsu
def visualizer():
    return render_template("visualizer/visual.html")


@app.route('/listview') 
def listview():
    return render_template("index.html")

@app.route('/admin')
def admin():
    print(session['username'])
    if session['username']!=app.username+app.secret_key or app.username=="":
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
    print(session['username'])
    if session['username']!=app.username+app.secret_key or app.username=="":
        return redirect(url_for('index'))
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
        keys = ['notam_series','notam_no','fir','scenario','nature','latin','longin','stimein','remarks','notam_type']
    else:
        keys = ['notam_series','notam_no','fir','ident','freq','latin','longin','stimein','remarks','notam_type']    
    notam_data = ""
    for key in keys:
        notam[key] = data[key]
        notam_data += " " + notam[key]
    notam['coords'] = []
    notam['coords'].append((notam['latin'],notam['longin']))
    notam_extract = extract.tags(notam_data)
    time = notam['stimein'].split('-')
    notam['start_time'] = time[0]
    notam['end_time'] = time[1]
    notam['issued_by'] = app.username
    time_start = notam['start_time'].split(' ')
    time_start.extend(time_start[0].split('-'))
    time_start.extend(time_start[1][:-2].split(':'))
    time_end = notam['end_time'].split(' ')
    time_end.extend(time_end[0].split('-'))
    time_end.extend(time_end[1][:-2].split(':'))
    time_start = datetime.datetime(*time_start)
    time_end = datetime.datetime(*time_end)
    delta_time = time_start - datetime.datetime.now() 
    if delta_time.total_seconds()>0:
        notam['status'] = 'Upcoming'
        delta_time = time_end - datetime.datetime.now()
    elif delta_time.total_seconds()>0:
        notam['status'] = 'Ongoing'
    else:
        notam['status'] = 'Expired'
    for key in notam_extract.keys():
        notam[key] = notam_extract[key]
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
    if database.add_user(user):
        return redirect(url_for('dashboard'))
    return redirect(url_for('index'))

@app.route('/verify_login',methods=['POST']) #User : SignUp
def verify_login():
    user = request.form
    user = user.to_dict(flat=False)
    for key in user.keys():
        user[key] = user[key][0]
    if database.verify_login(user):
        print("LOGIN SUCCESSFUL")
        app.username = user['email']
        session['username'] = user['email'] + app.secret_key 
        print(session['username'])
        return redirect(url_for('dashboard'))
    return redirect(url_for('index'))