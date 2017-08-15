from flask.ext.wtf import Form
from wtforms import StringField, BooleanField,TextField,PasswordField

class LoginForm(Form):
    name = StringField('name')
    passwd = PasswordField('passwd')
