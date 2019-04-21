# tuodaan tarvittavat osat
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, ValidationError, validators
from application.stats.models import Stat

# tämä luokka luo validaattorin, joka tarkistaa, että tilastoihin ei syötetä samalle pelaajalle useita merkintöjä yhteen otteluun
class Unique(object):
    def __init__(self, model, field, message=None):
        self.model = model
        self.field = field
        if not message:
            message = "Player's stats have already been given."
        self.message = message

    def __call__(self, form, field):
        check = self.model.query.filter(self.field == field.data, Stat.game_id == form.game_id.data).first()
        
        if check:
            raise ValidationError(self.message)


# lomake tilastojen syöttöä varten
class StatForm(FlaskForm):
    id = IntegerField("ID")
    game_id = IntegerField("game_id")
    player_id = SelectField("Player", [Unique(Stat, Stat.player_id)], coerce=int)
    goals = IntegerField("Goals", [validators.NumberRange(min=0)])
    assists = IntegerField("Assists", [validators.NumberRange(min=0)])
    penalties = IntegerField("Penalties", [validators.NumberRange(min=0)])

    class Meta:
        csrf = False