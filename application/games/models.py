# tuodaan tarvittavat osat
from application import db
from sqlalchemy.sql import text

# ottelua kuvaava luokka
class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    opponent = db.Column(db.String(32), nullable=False)
    our_goals = db.Column(db.Integer, nullable=False)
    opponent_goals = db.Column(db.Integer, nullable=False)

    teamname = db.Column(db.String(32), nullable=False)

    def __init__(self, date, opponent, our_goals, opponent_goals):
        self.date = date
        self.opponent = opponent
        self.our_goals = our_goals
        self.opponent_goals = opponent_goals