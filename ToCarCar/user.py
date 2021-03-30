from flask import Blueprint, flash, Flask, render_template, request, redirect
from db.user_db import *
from forms.FormClasses import *
user_bp = Blueprint('user_bp', __name__)

#API
@user_bp.route('/api/adduser', methods = ['POST'])
def new_user_api():
    first_name = request.form.get('firstName', 'Default')
    last_name = request.form.get('lastName', 'Default')
    email = request.form.get('email', 'Default')
    password = request.form.get('password', 'Default')
    user_type = 'USER'
        
    return add_user(first_name, last_name, email, password, user_type)
    