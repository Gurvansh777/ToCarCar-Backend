from flask import Blueprint, flash, Flask, render_template, request, url_for, redirect, session
from db.user_db import *
from forms.FormClasses import *
from user import user_bp
from constants import *
from bson.json_util import dumps

admin_bp = Blueprint('admin_bp', __name__)

client = MongoClient(MONGO_CLIENT_URL)
db = client[databaseName] #database

@admin_bp.route('/adminallusers', methods = ['GET', 'POST'])
def admin_allUsers():
    if session["loggedInEmail"] == adminEmail:
        allCustomers = db[userTableName].find({'userType': "USER"})
        auform = ApproveUserForm(prefix='approveuserform')
        return render_template('admin_home.html', allCustomers = allCustomers, auform = auform)
    else:    
        return render_template('index.html')
        
 
@admin_bp.route('/adminapproveuser', methods = ['GET', 'POST'])
def admin_approveUser():
    email = request.args.get('email')
    if(email is not None):
        update_user_approval_status(email, 1)
    return redirect(url_for('admin_bp.admin_allUsers'))
    
    
@admin_bp.route('/adminunapproveuser', methods = ['GET', 'POST'])
def admin_unapproveUser():
    email = request.args.get('email')
    if(email is not None):
        update_user_approval_status(email, 0)
    return redirect(url_for('admin_bp.admin_allUsers'))
    
    