# tuodaan tarvittavat osat
from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField
from wtforms.validators import Length

# uuden käyttäjän lomake
class UserForm(FlaskForm):

    teamname = StringField("Team's name", validators=[Length(min=2, max=48)])
    username = StringField("Username", validators=[Length(min=2, max=32)])
    password = PasswordField("Password", validators=[Length(min=2, max=32)])

    class Meta:
        csrf = False

# uuden peruskäyttäjän lomake
class RegularUserForm(FlaskForm):

    username = StringField("Username", validators=[Length(min=2, max=32)])
    password = PasswordField("Password", validators=[Length(min=2, max=32)])

    class Meta:
        csrf = False
