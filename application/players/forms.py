from flask_wtf import FlaskForm
from wtforms import Form, StringField, IntegerField, validators

class PlayerForm(FlaskForm):
    name = StringField("Player's name", [validators.Length(min=3)])
    number = IntegerField("Player's number", [validators.NumberRange(min=1, max=99)])

    class Meta:
        crsf = False