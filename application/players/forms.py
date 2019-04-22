# tuodaan tarvittavat osat
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, HiddenField, ValidationError, validators
from application.players.models import Player

# tämä luokka luo validaattorin, joka tarkistaa, että pelaajalle syötettyä numeroa ei ole varattu
class Unique(object):
    def __init__(self, model, field, message=None):
        self.model = model
        self.field = field
        if not message:
            message = "Number has already taken."
        self.message = message

    def __call__(self, form, field):
        check = self.model.query.filter(self.field == field.data, Player.teamname == form.teamname.data).first()
        if 'id' in form:
            id = form.id.data
        else:
            id = None
        if check and (id is None or id != check.id):
            raise ValidationError(self.message)


# lomake pelaajan tietojen keruuta varten
class PlayerForm(FlaskForm):
    id = IntegerField("ID")
    teamname = StringField("teamname")
    number = IntegerField("Player's number", [validators.NumberRange(min=1, max=99), Unique(Player, Player.number)])
    name = StringField("Player's name", [validators.Length(min=3, max=48)])

    class Meta:
        csrf = False

# lomake pelaajan tietojen hakua varten
class queryForm(FlaskForm):
    name = StringField("Player's name", [validators.Length(min=1)])

    class Meta:
        csrf = False
