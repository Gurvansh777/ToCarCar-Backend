from flask_wtf import FlaskForm
from wtforms import TextField, PasswordField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    email = TextField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    login = SubmitField('Login')
    
class RegistrationForm(FlaskForm):
    first_name = TextField('First Name', validators=[DataRequired()])
    last_name = TextField('Last Name', validators=[DataRequired()])
    email = TextField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('ConfirmPassword', validators=[DataRequired()])
    add_user = SubmitField('Add User')