from flask import jsonify
from pymongo import MongoClient
import constants

client = MongoClient(constants.MONGO_CLIENT_URL)
db = client.tocarcar #database

def add_user(first_name, last_name, email, password):
    if db.users.find({'email': email}).count() == 0:
        user = {'firstName' : first_name, 'lastName' : last_name, 'email' : email, 'password' : password}
        db.users.insert_one(user)
        return jsonify(useradded = 1, email = email, message = 'user added!')
    else:
        return jsonify(useradded = 0, email = email, message = 'user already exist!')
        

def check_credentials(email, password):
    if db.users.find({'email' : email, 'password' : password}).count() > 0:
        return jsonify(uservalid = 1, message = 'user is valid!')
    else:
        return jsonify(usevalid = 0, message = 'user is invalid!')