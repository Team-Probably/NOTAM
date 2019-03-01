import pymongo
import os
from pymongo import MongoClient

#mongodb_url = str(os.environ["NOTAMS_MONGODB"])
#mongod --dbpath "/home/rusherrg/Projects/SIH/webapp/database" --port 10000
mongodb_url = 'mongodb://localhost:10000/' 

def connect():
    client = MongoClient(mongodb_url)
    db = client.notams
    return db

def add_notam(notam):
    db = connect()
    if notam['notam_type'] == "airspace":
        db = db.airspace
    if notam['notam_type'] == "facility":
        db = db.facility
    if db.find_one(notam):
        print("Already Present")
        return 0
    db.insert(notam)
    return 1

def get_notams(notam_type):
    db = connect()
    if notam_type == "airspace":
        db = db.airspace
    if notam_type == "facility":
        db = db.facility
    notams = []
    print("Getting NOTAMs")
    for notam in db.find():
        notams.append(notam)
    return notams

def remove_notam(notam):
    db = connect()
    if notam['notam_type'] == "airspace":
        db = db.airspace
    if notam['notam_type'] == "facility":
        db = db.facility
    if db.find_one(notam):
        db.delete_one(notam)
        print("NOTAM Deleted")
    else:
        print("NOTAM not Present")
    return

def add_user(user):
    db = connect()
    db = db.users
    if db.find_one(user):
        return 0
    db.insert(user)
    print(user, "USER CREATED")
    return 1

def verify_login(user):
    db = connect()
    db = db.users
    if db.find_one(user):
        print(user, "LOGIN SUCCESSFUL")
        return 1
    return 0