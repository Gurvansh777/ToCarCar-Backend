from flask import jsonify
from pymongo import MongoClient
from constants import *

client = MongoClient(MONGO_CLIENT_URL)
db = client.tocarcar #database

def add_user(first_name, last_name, email, password, user_type):
    if db.users.find({'email': email}).count() == 0:
        user = {'firstName' : first_name, 'lastName' : last_name, 'email' : email, 'password' : password, 'userType' : user_type}
        db.users.insert_one(user)
        
        return jsonify(useradded = 1, email = email, message = 'user added!')
    else:
        return jsonify(useradded = 0, email = email, message = 'user already exist!')
        

def check_credentials(email, password):
    user = db.users.find_one({'email' : email, 'password' : password})
    return user
    