from flask_wtf import FlaskForm
from wtforms import TextField, PasswordField, SubmitField

class LoginForm(FlaskForm):
    email = TextField('Email')
    password = PasswordField('Password')
    login = SubmitField('Login')
    
class RegistrationForm(FlaskForm):
    first_name = TextField('First Name')
    last_name = TextField('Last Name')
    email = TextField('Email')
    password = PasswordField('Password')
    confirm_password = PasswordField('ConfirmPassword')
    add_user = SubmitField('Add User')