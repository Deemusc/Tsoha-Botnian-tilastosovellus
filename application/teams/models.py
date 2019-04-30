# tuodaan tarvittavat osat
from application import db

# joukkuetta kuvaava luokka
class Team(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), nullable=False, unique=True)

    accounts = db.relationship("User", backref='team', lazy=True)
    games = db.relationship("Game", backref='team', lazy=True)
    players = db.relationship("Player", backref='team', lazy=True)

    def __init__(self, name):
        self.name = name
