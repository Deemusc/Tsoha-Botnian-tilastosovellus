# tarvittavat importit
from flask_wtf import FlaskForm
from wtforms import IntegerField, DateField, StringField, validators

# ottelun lomake
class GameForm(FlaskForm):
    id = IntegerField("ID")
    date = DateField("Date (yyyy-mm-dd)", [validators.DataRequired(message="Insert date as yyyy-mm-dd.")])
    opponent = StringField("Opponent", [validators.Length(min=2, max=32, message="Name is too short or long (2-32 characters).")])
    our_goals = IntegerField("Our goals", [validators.NumberRange(min=0, message="Amount of goals can't be negative.")])
    opponent_goals = IntegerField("Opponent's goals", [validators.NumberRange(min=0, message="Amount of goals can't be negative.")])

    class Meta:
        csrf = False

# lomake tietyn ottelun hakemiseen
class queryGameForm(FlaskForm):
    opponent = StringField("Opponent's name", [validators.Length(min=1, max=32, message="Enter at least one character (maximum is 32).")])

    class Meta:
        csrf = False
