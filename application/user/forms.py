from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField
from wtforms.validators import Length

class UserForm(FlaskForm):

    name = StringField("Name", validators=[Length(min=2, max=32)])
    username = StringField("Username", validators=[Length(min=2, max=32)])
    password = PasswordField("Password", validators=[Length(min=2, max=32)])

    class Meta:
        csrf = False
