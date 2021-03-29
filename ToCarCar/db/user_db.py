from flask import jsonify
from pymongo import MongoClient
from constants import *

client = MongoClient(MONGO_CLIENT_URL)
db = client.tocarcar #database

def add_user(first_name, last_name, email, password, user_type):
    if db.users.find({'email': email}).count() == 0:
        user = {'firstName' : first_name, 'lastName' : last_name, 'email' : email, 'password' : password, 'userType' : user_type, 'isApproved' : 0}
        db.users.insert_one(user)
        
        return jsonify(useradded = 1, email = email, message = 'user added!')
    else:
        return jsonify(useradded = 0, email = email, message = 'user already exist!')
        

def check_credentials(email, password):
    user = db.users.find_one({'email' : email, 'password' : password})
    return user


def get_user_by_email(email):
    user = db.users.find_one({'email' : email})
    return user
    
    
def update_user_approval_status(email, approvalStatus):
    query = {'email': email}
    newValue = { '$set': {
                        'isApproved': approvalStatus
                    } 
                }
    
    db[userTableName].update_one(query, newValue)
    
    
def update_posting_approval_status(licensePlate, dateFrom, dateTo, approvalStatus):
    query = {'licensePlate': licensePlate, 'dateFrom': dateFrom, 'dateTo': dateTo}
    newValue = { '$set': {
                        'isApproved': approvalStatus
                    } 
                }
    
    db[postingTableName].update_one(query, newValue)