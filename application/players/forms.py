from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, validators

class PlayerForm(FlaskForm):
    id = IntegerField("ID")
    number = IntegerField("Player's number", [validators.NumberRange(min=1, max=99)])
    name = StringField("Player's name", [validators.Length(min=3)])

    class Meta:
        csrf = False

class queryForm(FlaskForm):
    name = StringField("Player's name", [validators.Length(min=1)])

    class Meta:
        csrf = False