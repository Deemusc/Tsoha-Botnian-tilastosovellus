from flask_wtf import FlaskForm
from wtforms import IntegerField, DateField, StringField, validators

class GameForm(FlaskForm):
    date = DateField("Date (yyyy-mm-dd)", [validators.DataRequired(message="Date required.")])
    opponent = StringField("Opponent", [validators.Length(min=2, max=32)])
    botnia_goals = IntegerField("Botnia's goals", [validators.NumberRange(min=0)])
    opponent_goals = IntegerField("Opponent's goals", [validators.NumberRange(min=0)])
