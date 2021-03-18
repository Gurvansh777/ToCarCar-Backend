from flask import Blueprint, flash, Flask, render_template, request, redirect
from db.user_db import *
from forms.FormClasses import *
user_bp = Blueprint('user_bp', __name__)

#WEB
@user_bp.route('/adduser', methods = ['GET', 'POST'])
def new_user():
    rform = RegistrationForm(prefix='registrationform')
    if rform.validate_on_submit() and rform.validate():
        return new_user_submit(rform) 
    return render_template('user_registration.html', rform = rform)
    
def new_user_submit(rform):
    first_name = rform.first_name.data
    last_name = rform.last_name.data
    email = rform.email.data
    password = rform.password.data
    confirm_password = rform.confirm_password.data
    user_type = "USER"
    
    if get_user_by_email(email) is None:
        add_user(first_name, last_name, email, password, user_type)
        flash("User added! Please login to continue")
    else:
        flash("This email is already registered!")
        return redirect("/adduser")

#API
@user_bp.route('/api/adduser', methods = ['POST'])
def new_user_api():
    first_name = request.form.get('firstName', 'Default')
    last_name = request.form.get('lastName', 'Default')
    email = request.form.get('email', 'Default')
    password = request.form.get('password', 'Default')
    user_type = 'USER'
        
    return add_user(first_name, last_name, email, password, user_type)
    