import pymongo
import os
from pymongo import MongoClient

mongodb_url = str(os.environ["NOTAMS_MONGODB"])

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
        return
    db.insert(notam)
    print("NOTAM Inserted")
    return

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

    