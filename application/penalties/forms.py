from flask_wtf import FlaskForm
from wtforms import IntegerField, SelectField, validators

class PenaltyForm(FlaskForm):
    id = IntegerField("ID")
    game_id = IntegerField("game_id")
    player_number = IntegerField("Player (#)", [validators.NumberRange(min=1, max=99, message="Number has to be between 1-99.")])
    minutes = SelectField("Penalty minutes", choices=[('2', '2 min'), ('5', '5 min'), ('10', '10 min'), ('25', '25 min')])

    class Meta:
        csrf = False
