# tuodaan tarvittavat osat
from flask_wtf import FlaskForm
from wtforms import StringField, HiddenField, ValidationError, validators
from application.teams.models import Team

class Unique(object):
    def __init__(self, model, field, message=None):
        self.model = model
        self.field = field
        if not message:
            message = "Team has already admin user."
        self.message = message

    def __call__(self, form, field):
        check = self.model.query.filter(self.field == field.data).first()
        if check:
            raise ValidationError(self.message)    

# uuden adminkäyttäjän joukkueen lomake
class TeamForm(FlaskForm):

    name = StringField("Team's name", [validators.Length(min=2, max=32), Unique(Team, Team.name)])

    class Meta:
        csrf = False
