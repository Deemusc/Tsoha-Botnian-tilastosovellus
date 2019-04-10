from flask_wtf import FlaskForm
from wtforms import IntegerField, SelectField, validators

class GoalForm(FlaskForm):
    id = IntegerField("ID")
    game_id = IntegerField("game_id")
    scorer_number = IntegerField("Goal scorer (#)", [validators.NumberRange(min=0, max=99, message="Number has to be between 1-99.")])
    assist_number = IntegerField("Goal assist (#)", [validators.NumberRange(min=0, max=99, message="Number has to be between 1-99.")])

    #scorer_number = SelectField("Goal scorer (#)", choices=[('1', 'player')])
    #assist_number = SelectField("Goal assist (#)", choices=[('1', 'player')])



    class Meta:
        csrf = False
