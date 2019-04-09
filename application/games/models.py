from application import db
from sqlalchemy.sql import text

# aputaulu
gameplayers = db.Table("gameplayers",
            db.metadata,            
            db.Column("player_id", db.Integer, db.ForeignKey("player.id")),
            db.Column("game_id", db.Integer, db.ForeignKey("game.id"))
            )

class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    opponent = db.Column(db.String(32), nullable=False)
    botnia_goals = db.Column(db.Integer, nullable=False)
    opponent_goals = db.Column(db.Integer, nullable=False)

    players = db.relationship('Player',
                secondary=gameplayers, 
                back_populates="games")

    def __init__(self, date, opponent, botnia_goals, opponent_goals):
        self.date = date
        self.opponent = opponent
        self.botnia_goals = botnia_goals
        self.opponent_goals = opponent_goals
