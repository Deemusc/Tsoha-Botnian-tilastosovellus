# tuodaan tarvittavat osat
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, RadioField, BooleanField, SelectField, validators

# lomake tilastojen syöttöä varten
class StatForm(FlaskForm):
    id = IntegerField("ID")
    game_id = IntegerField("game_id")
    player_id = SelectField("Player", coerce=int)
    goals = IntegerField("Goals", [validators.NumberRange(min=0)])
    assists = IntegerField("Assists", [validators.NumberRange(min=0)])
    penalties = IntegerField("Penalties", [validators.NumberRange(min=0)])

    class Meta:
        csrf = False