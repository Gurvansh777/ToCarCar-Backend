"""
Main file of the project to handle user authentication
"""
from flask import Flask, flash, render_template, request, url_for, redirect, session
from db.user_db import *
from forms.FormClasses import *
from user import user_bp
from admin import admin_bp
from apiHelper import apiHelper_bp
from constants import *
from bson.json_util import dumps


app = Flask(__name__)
app.config.update(dict(SECRET_KEY='yoursecretkey'))
app.register_blueprint(user_bp)
app.register_blueprint(admin_bp)
app.register_blueprint(apiHelper_bp)



client = MongoClient(MONGO_CLIENT_URL)
db = client[databaseName] #database



#expose / - root
@app.route('/', methods = ['GET'])
def init():
    if db[userTableName].find({'email': 'admin@example.com'}).count() <= 0:
        db[userTableName].insert_one({'firstName' : "Admin", 'lastName' : "Harman", 'email' : adminEmail, 'password' : "Admin", 'userType' : 'ADMIN', 'isApproved': 1})
        
    return redirect(url_for('check_user'))

#WEB function to verify user
@app.route('/checkuser', methods = ['GET', 'POST'])
def check_user():
    lform = LoginForm(prefix='loginform')
    if lform.validate_on_submit() and lform.validate():
        return check_user_submit(lform) 
    return render_template('index.html', lform = lform)
    
def check_user_submit(lform):
    email = lform.email.data
    password = lform.password.data
    user = check_credentials(email, password)
    if user is not None:
        session['loggedInEmail'] = user['email']
        return redirect(url_for('admin_bp.admin_allUsers'))
    else:
        flash('Invalid user!')
        return redirect("/")
        
#API - verify user in the android application
@app.route('/api/checkuser', methods = ['POST'])
def check_user_api():
    email = request.form.get('email', 'Default')
    password = request.form.get('password', 'Default')
        
    user = check_credentials(email, password)
    if(user is None):
        return jsonify(uservalid = 0, message = 'user is invalid!')
    else:
        return jsonify(uservalid = 1, message = 'user is valid!', firstName = user['firstName'], lastName = user['lastName'], isApproved = user['isApproved'])


if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
