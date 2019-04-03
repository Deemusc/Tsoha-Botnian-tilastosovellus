from flask_wtf import Form
from wtforms import IntegerField
from wtforms.validators import NumberRange

class GoalForm(Form):
    id = IntegerField("ID")
    game_id = IntegerField("game_id")
    scorer_number = IntegerField("Goal scorer (#)", validators=[NumberRange(min=0, max=99)])
    assist_number = IntegerField("Goal assist (#)", validators=[NumberRange(min=0, max=99)])

    class Meta:
        csrf = False
