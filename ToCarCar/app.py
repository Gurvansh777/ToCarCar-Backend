from flask import Flask, render_template, request, url_for, redirect
from db.user_db import *
from forms.FormClasses import *
from user import user_bp

app = Flask(__name__)
app.config.update(dict(SECRET_KEY='yoursecretkey'))
app.register_blueprint(user_bp)

#expose /
@app.route('/', methods = ['GET'])
def init():
    return redirect(url_for('check_user'))

#WEB
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
        if user['userType'] == 'ADMIN':
            return render_template('admin_home.html', user = user)
        else:
            return render_template('user_home.html', user = user)
    else:
        return redirect("/")
        
#API
@app.route('/api/checkuser', methods = ['POST'])
def check_user_api():
    email = request.form.get('email', 'Default')
    password = request.form.get('password', 'Default')
        
    user = check_credentials(email, password)
    if(user is None):
        return jsonify(uservalid = 0, message = 'user is invalid!')
    else:
        return jsonify(uservalid = 1, message = 'user is valid!', firstName = user['firstName'], lastName = user['lastName'])

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
