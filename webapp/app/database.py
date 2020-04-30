import pymongo
import os
import datetime
import ast
import pprint
from pymongo import MongoClient
#mongodb_remote_url = str(os.environ["NOTAMS_MONGODB"])
# mongod --dbpath "/home/rusherrg/Projects/SIH/webapp/database" --port 10000
mongodb_local_url = os.getenv('MONGODB_URI')


def connect(uri):
    client = MongoClient(uri)
    db = client.notams
    return db


def add_notam(notam):
    db = connect(mongodb_local_url)
    if notam['notam_type'] == "airspace":
        db = db.airspace
    if notam['notam_type'] == "facility":
        db = db.facility
    if db.find_one({'notam_no': notam['notam_no'], 'notam_series': notam['notam_series']}):
        print("Already Present")
        return 0
    db.insert(notam)
    return 1


def edit_notam(notam):
    db = connect(mongodb_local_url)
    if notam['notam_type'] == "airspace":
        db = db.airspace
    if notam['notam_type'] == "facility":
        db = db.facility
    if db.find_one({'notam_no': notam['notam_no'], 'notam_series': notam['notam_series']}):
        print(notam, db)
        # remove_notam(notam)
        # add_notam(notam)
    return notam


def get_notams(notam_type):
    db = connect(mongodb_local_url)
    if notam_type == "airspace":
        db = db.airspace
    if notam_type == "facility":
        db = db.facility
    notams = []
    print("Getting NOTAMs")
    for notam in db.find():
        st = datetime.datetime(
            *list(map(int, notam['stime'].split(' ')[0].split('/')+notam['stime'].split(' ')[1].split(':'))))
        et = datetime.datetime(
            *list(map(int, notam['etime'].split(' ')[0].split('/')+notam['etime'].split(' ')[1].split(':'))))
        now = datetime.datetime.now()
        if st > now:
            notam['status'] = "Upcoming"
        elif et < now:
            notam['status'] = "Expired"
        else:
            notam['status'] = "Ongoing"
        notams.append(notam)
    return notams


def get_notam(key, value):
    notam = {key: value}
    db = connect(mongodb_local_url)
    if db.airspace.find_one(notam):
        notam = db.airspace.find_one(notam)
        return notam
    if db.facility.find_one(notam):
        notam = db.airspace.find_one(notam)
        return notam
    return "NOT FOUND"


def remove_notam(key, value):
    db = connect(mongodb_local_url)
    notam = {key: value}
    if db.airspace.find_one(notam):
        try:
            db.airspace.delete_one(notam)
            return "NOTAM DELETED"
        except:
            return "ERROR"
    if db.facility.find_one(notam):
        try:
            db.facility.delete_one(notam)
            return "NOTAM DELETED"
        except:
            return "ERROR"
    return "NOTAM NOT FOUND"


def add_user(user):
    db = connect(mongodb_local_url)
    db = db.users
    if db.find_one(user):
        return 0
    db.insert(user)
    print(user, "USER CREATED")
    return 1


def verify_login(user):
    db = connect(mongodb_local_url)
    db = db.users
    if db.find_one(user):
        print(user, "LOGIN SUCCESSFUL")
        return db.find_one(user)
    return 0


def populate():
    with open('./notams.txt', 'r') as f:
        notams = f.readlines()
        for notam in notams:
            pprint.pprint(eval(notam))
            add_notam(eval(notam))
    return


def mongodb_push():
    remote = connect(mongodb_remote_url)
    local = connect(mongodb_local_url)
    collections = local.collection_names()
    for coll in collections:
        for data in list(local[coll].find()):
            if list(remote[coll].find(data)) != []:
                remote[coll].insert(data)
    return


def mongodb_pull():
    remote = connect(mongodb_remote_url)
    local = connect(mongodb_local_url)
    collections = local.collection_names()
    for coll in collections:
        for data in list(remote[coll].find()):
            if list(local[coll].find(data)) != []:
                local[coll].insert(data)
    return
