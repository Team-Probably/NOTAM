import pymongo
import os,datetime
from pymongo import MongoClient
# mongodb_remote_url = str(os.environ["NOTAMS_MONGODB"])
#mongod --dbpath "/home/rusherrg/Projects/SIH/webapp/database" --port 10000
mongodb_local_url = 'mongodb://localhost:10000/' 

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
    if db.find_one({'notam_no':notam['notam_no'],'notam_series':notam['notam_series']}):
        print("Already Present")
        return 0
    db.insert(notam)
    return 1

def get_notams(notam_type):
    db = connect(mongodb_local_url)
    if notam_type == "airspace":
        db = db.airspace
    if notam_type == "facility":
        db = db.facility
    notams = []
    print("Getting NOTAMs")
    for notam in db.find():
    #     time = notam['stimein'].split('-')
    #     notam['start_time'] = time[0]
    #     notam['end_time'] = time[1]
    #     time_start = notam['start_time'].split(' ')
    #     time_start.extend(time_start[0].split('-'))
    #     time_start.extend(time_start[1][:-2].split(':'))
    #     time_end = notam['end_time'].split(' ')
    #     time_end.extend(time_end[0].split('-'))
    #     time_end.extend(time_end[1][:-2].split(':'))
    #     time_start = datetime.datetime(*time_start)
    #     time_end = datetime.datetime(*time_end)
    #     delta_time = time_start - datetime.datetime.now() 
    #     if delta_time.total_seconds()>0:
    #         notam['status'] = 'Upcoming'
    #         delta_time = time_end - datetime.datetime.now()
    #     elif delta_time.total_seconds()>0:
    #         notam['status'] = 'Ongoing'
    #     else:
    #         notam['status'] = 'Expired'
        notams.append(notam)
    return notams

def remove_notam(notam):
    db = connect(mongodb_local_url)
    if notam['notam_type'] == "airspace":
        db = db.airspace
    if notam['notam_type'] == "facility":
        db = db.facility
    if db.find_one({'notam_no':notam['notam_no'],'notam_series':notam['notam_series']}):
        try:
            db.delete_one(notam)
        except:
            print("ERROR")
        print("NOTAM Deleted")
    else:
        print("NOTAM not Present")
    return

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
        return 1
    return 0

def mongodb_push():
    remote = connect(mongodb_remote_url)
    local = connect(mongodb_local_url)
    collections = local.collection_names()
    for coll in collections:
        for data in list(local[coll].find()):
            if list(remote[coll].find(data))!=[]:
                remote[coll].insert(data)
    return

def mongodb_pull():
    remote = connect(mongodb_remote_url)
    local = connect(mongodb_local_url)
    collections = local.collection_names()
    for coll in collections:
        for data in list(remote[coll].find()):
            if list(local[coll].find(data))!=[]:
                local[coll].insert(data)
    return
    
            