# views.py
from flask import render_template,request,Response
import json
from app import app
from app import extract
from app import database

@app.route('/') #TO-DO : By Aditya and Avi 
def index():
    return render_template("index.html")


@app.route('/visualizer') #TO-DO : By Kiteretsu
def visualizer():
    return render_template("visualizer/visual.html")


@app.route('/listview')  # TO-DO : By Hatel di
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
    keys = ['notam_series','notam_no','fir','scenario','nature','latin','longin','stimein','endtimein','remarks']
    data = request.get_json()
    for key in keys:
        notam[key] = data[key]
    notam['notam_type'] = 'airspace'
    print(notam)
    if database.add_notam(notam):
        return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}
    else:
        return json.dumps({'success': "NOTAM Exists"}), 200, {'ContentType': 'application/json'}
    
