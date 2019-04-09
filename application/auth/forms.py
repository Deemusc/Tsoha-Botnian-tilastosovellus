from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators

class LoginForm(FlaskForm):
    username = StringField("Username", [validators.Length(min=3, max=32, message="No such username or password.")])
    password = PasswordField("Password", [validators.Length(min=3, max=32, message="No such username or password.")])

    class Meta:
        csrf = False
