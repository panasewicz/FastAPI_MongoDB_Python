import pymongo, models

mongoURI = "mongodb://localhost:27017"
client = pymongo.MongoClient(mongoURI)

db = client["Zadanie_Projekt"]
collection_students = db["students"]
collection_messages = db["messages"]

#pymongo Students
def create(data):
    data = dict(data)
    response = collection_students.insert_one(data)
    return str(response.inserted_id)

def all():
    response = collection_students.find({})
    data = []
    for i in response:
        i["_id"] = str(i["_id"])
        data.append(i)
    return data

def update(data):
    data = dict(data)
    response = collection_students.update_one({"name":data["name"]}, {"$set":{"lastname":data["lastname"]}})
    return response.modified_count

def delete(name):
    response = collection_students.delete_one({"name":name})
    return response.deleted_count

#pymongo Messages
def create2(data):
    data = dict(data)
    response = collection_messages.insert_one(data)
    return str(response.inserted_id)

def get_all_messages(condition, condition2, condition3):
    from operator import itemgetter
    response = collection_messages.find({"studentId":condition , "name":condition2 , "lastname":condition3})
    data = []
    data2 = []
    for i in response:
        i["_id"] = str(i["_id"])
        data.append(i)
        a = itemgetter("_id", "message")(i)
        data2.append(a)
    return data2

def get_student(condition):
    from bson.objectid import ObjectId
    from operator import itemgetter
    _id = ObjectId(condition)
    response = collection_messages.find_one({("_id"):_id})
    response["_id"] = str(["_id"])
    a = itemgetter("name", "lastname", "studentId")(response)
    return a






