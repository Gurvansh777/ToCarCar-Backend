from flask import Blueprint, Flask, render_template, redirect, request
from pymongo import MongoClient
from constants import *
from bson.json_util import dumps
import json
from bson import ObjectId, BSON


apiHelper_bp = Blueprint('apiHelper_bp', __name__)


client = MongoClient(MONGO_CLIENT_URL)
db = client.tocarcar #database


#Headers -  Content-Type: application/json
#           objectName: tasks
@apiHelper_bp.route('/api/getallrecords', methods = ['GET', 'POST'])
def getAllRecords():
    objectName = request.headers["objectName"]
    data = db[objectName].find({})
    listData = list(data)
    json_data = dumps(listData)
    return json_data
    
    
    

@apiHelper_bp.route('/api/getspecificrecords', methods = ['GET', 'POST'])
def getSpecificRecords():
    objectName = request.headers["objectName"]
    query = request.json
    print("\n")
    print(query)
    query = json.loads(query)
    print("\n")
    print(query)
    data = db[objectName].find(query)
    listData = list(data)
    json_data = dumps(listData)
    return json_data
    
    


#Body

#   {
#       "id": 2,
#       "title": "Test 2",
#       "shortdesc": "test",
#       "priority": 2
#   }

@apiHelper_bp.route('/api/addrecord', methods = ['POST'])
def addRecord():
    recordToInsert = request.json
    objectName = request.headers["objectName"]
    recordToInsert = json.loads(recordToInsert)
    db[objectName].insert(recordToInsert)
    return getAllRecords()
    
    
#Body

#   {
#       "id": 2
#   }
@apiHelper_bp.route('/api/delete', methods = ['GET', 'POST'])
def delete():
    recordsToDelete = request.json
    objectName = request.headers["objectName"]
    db[objectName].delete_many(recordsToDelete)
    return getAllRecords()




#Body

#   {
#       "myQuery": {
#           "id": 10
#       },
#       "newValues": {
#            "$set": {
#               "id": 1,
#                "title": "Test 1",
#                "shortdesc": "test",
#                "priority": 1
#           }
#        }
#   }
@apiHelper_bp.route('/api/updaterecord', methods = ['GET', 'POST'])
def updateRecord():
    requestBody = request.json
    print("requestBody" + requestBody)
    requestBody = json.loads(requestBody)
    myQuery = requestBody["myQuery"]
    print("\n")
    print(myQuery)
    newValues = requestBody["newValues"]
    print("\n")
    print(newValues)
    objectName = request.headers["objectName"]
    
    db[objectName].update_one(myQuery, newValues)
    
    return getAllRecords()    
    
    
if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
