# views.py
from flask import render_template,request

from app import app
import extract
import database

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
    return render_template('admin.html')


@app.route('/processor', methods=['POST'])  # TO-DO : By Rushang and akshay
def processor():

    return Response(
            json.dumps(
                    extract.extract('NOTAM.pdf')
                ), mimetype='application/json'
            )

@app.route('/dashboard') #USER : Notam Lists
def dashboard():
    airspace = get_notams('airspace')
    facility = get_notams('facility')
    return render_template("dashboard.html", facility = facility , airspace = airspace)

@app.route('/create_notam') #Admin : Create Notams
def create():
    notam = {}
    keys = ['notam_series','notam_no','fir','scenario','nature','coords','time','remarks']
    for key in keys:
        notam[key] = request.form(key)
    print(notam)
    add_notam(notam)
    return render_template(str(notam))
    