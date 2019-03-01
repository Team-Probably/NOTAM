# views.py
from flask import render_template,request,Response,redirect,url_for
import json
from app import app
from app import extract
from app import database
from werkzeug.datastructures import ImmutableMultiDict

@app.route('/') #TO-DO : By Aditya and Avi 
def index():
    return render_template("login.html")    


@app.route('/visualizer') #TO-DO : By Kiteretsu
def visualizer():
    return render_template("visualizer/visual.html")


@app.route('/listview') 
def listview():
    return render_template("index.html")

@app.route('/admin')
def admin():
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
    return render_template("dashboard.html", facility = facility , airspace = airspace)

@app.route('/create_notam',methods=['POST']) #Admin : Create Notams
def create():
    notam = {}
    keys = ['notam_series','notam_no','fir','scenario','nature','latin','longin','stimein','remarks']
    data = request.get_json()
    notam_data = ""
    for key in keys:
        notam[key] = data[key]
        notam_data += " " + notam[key]
    notam['coords'] = []
    for i, j in zip(notam['latin'], notam['longin']):
        notam['coords'].append((i,j))
    notam_extract = extract.tags(notam_data)
    for key in notam_extract.keys():
        notam[key] = notam_extract[key]
    notam['notam_type'] = 'airspace'
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
    return render_template('login.html')

@app.route('/verify_login',methods=['POST']) #User : SignUp
def verify_login():
    user = request.form
    user = user.to_dict(flat=False)
    for key in user.keys():
        user[key] = user[key][0]
    if database.verify_login(user):
        return redirect(url_for('dashboard'))
    return render_template('login.html')
    
