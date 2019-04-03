from flask_wtf import Form
from wtforms import IntegerField, DateField, StringField
from wtforms.validators import NumberRange, Length, DataRequired

class GameForm(Form):
    id = IntegerField("ID")
    date = DateField("Date (yyyy-mm-dd)", validators=[DataRequired(message="Insert date as yyyy-mm-dd.")])
    opponent = StringField("Opponent", validators=[Length(min=2, max=32)])
    botnia_goals = IntegerField("Botnia's goals", validators=[NumberRange(min=0)])
    opponent_goals = IntegerField("Opponent's goals", validators=[NumberRange(min=0)])
    

    class Meta:
        csrf = False

class queryGameForm(Form):
    opponent = StringField("Opponent's name", validators=[Length(min=2, max=32)])

    class Meta:
        csrf = False