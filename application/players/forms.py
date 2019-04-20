# tuodaan tarvittavat osat
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, RadioField, BooleanField, validators

# lomake pelaajan tietojen keruuta varten
class PlayerForm(FlaskForm):
    id = IntegerField("ID")
    number = IntegerField("Player's number", [validators.NumberRange(min=1, max=99)])
    name = StringField("Player's name", [validators.Length(min=3, max=48)])

    class Meta:
        csrf = False

# lomake pelaajan tietojen hakua varten
class queryForm(FlaskForm):
    name = StringField("Player's name", [validators.Length(min=1)])

    class Meta:
        csrf = False

class addToGameForm(FlaskForm):
    game_id = IntegerField("game_id")
    player_number = IntegerField("Player's number", [validators.NumberRange(min=1, max=99)])
