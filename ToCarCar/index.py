from flask import Flask, render_template, request
from user_management import *

app = Flask(__name__)

#expose /
@app.route('/', methods = ['GET'])
def init():
    return "Welcome to 2CarCar"

#if GET show index else process new user
@app.route('/adduser', methods = ['GET', 'POST'])
def main():
    if request.method == 'POST':
        first_name = request.form.get('firstName', 'Default')
        last_name = request.form.get('lastName', 'Default')
        email = request.form.get('email', 'Default')
        password = request.form.get('password', 'Default')
        
        return add_user(first_name, last_name, email, password) #in user_management.py
    else:
        return render_template('index.html')

#expose /checkuser
@app.route('/checkuser', methods = ['POST'])
def check_user():
    if request.method == 'POST':
        email = request.form.get('email', 'Default')
        password = request.form.get('password', 'Default')
        
        return check_credentials(email, password) #in user_management.py
    else:
        return render_template('index.html')
        

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
