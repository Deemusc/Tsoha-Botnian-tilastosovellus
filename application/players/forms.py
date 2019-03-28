from flask_wtf import Form
from wtforms import StringField, IntegerField
from wtforms.validators import NumberRange, Length

class PlayerForm(Form):
    id = IntegerField("ID")
    number = IntegerField("Player's number", validators=[NumberRange(min=1, max=99)])
    name = StringField("Player's name", validators=[Length(min=3)])

    class Meta:
        csrf = False

class queryForm(Form):
    name = StringField("Player's name", validators=[Length(min=3)])

    class Meta:
        csrf = False