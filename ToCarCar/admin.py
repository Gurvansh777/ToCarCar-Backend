from flask import Blueprint, flash, Flask, render_template, request, url_for, redirect, session
from db.user_db import *
from forms.FormClasses import *
from user import user_bp
from constants import *
from bson.json_util import dumps

admin_bp = Blueprint('admin_bp', __name__)

client = MongoClient(MONGO_CLIENT_URL)
db = client[databaseName] #database

#########################ALL USERS#################################
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
  
  
#########################NEW POSTINGS########################################
@admin_bp.route('/adminallpostings', methods = ['GET', 'POST'])
def admin_allPostings():
    if session["loggedInEmail"] == adminEmail:
        allPostings = db[postingTableName].find({})
        return render_template('admin_new_postings.html', allPostings = allPostings)
    else:    
        return render_template('index.html')

@admin_bp.route('/adminapproveposting', methods = ['GET', 'POST'])
def admin_approvePosting():
    licensePlate = request.args.get('licensePlate')
    dateFrom = request.args.get('dateFrom')
    dateTo = request.args.get('dateTo')
    
    if(licensePlate is not None):
        update_posting_approval_status(licensePlate, dateFrom, dateTo, 1)
    return redirect(url_for('admin_bp.admin_allPostings'))
    
    
@admin_bp.route('/adminunapproveposting', methods = ['GET', 'POST'])
def admin_unapprovePosting():
    licensePlate = request.args.get('licensePlate')
    dateFrom = request.args.get('dateFrom')
    dateTo = request.args.get('dateTo')
    
    if(licensePlate is not None):
         update_posting_approval_status(licensePlate, dateFrom, dateTo, 0)
    return redirect(url_for('admin_bp.admin_allPostings'))