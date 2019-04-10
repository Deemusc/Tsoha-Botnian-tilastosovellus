from application import db
from application.games.models import gameplayers
from sqlalchemy.sql import text

# Varsinainen pelaajaluokka
class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)    
    number = db.Column(db.Integer, nullable=False, unique=True)
    name = db.Column(db.String(48), nullable=False)

    games = db.relationship("Game",
                secondary=gameplayers,
                back_populates="players")

    penalties = db.relationship("Penalty", backref="player", lazy=True)

    goals = db.relationship("Goal", backref="player", lazy=True)

    def __init__(self, name, number):
        self.name = name
        self.number = number 



    @staticmethod
    def list_goal_scorers():
        stmt = text("SELECT Player.number, Player.name, COUNT(Goal.scorer_id) AS goals"
                    " FROM Player"
                    " INNER JOIN Goal ON Goal.scorer_id=Player.id"
                    " GROUP BY Player.number, Player.name, Goal.scorer_id"
                    " ORDER BY goals DESC;")
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"number":row[0], "name":row[1], "goals":row[2]})

        return response

    @staticmethod
    def list_assists():
        stmt = text("SELECT Player.number, Player.name, COUNT(Goal.assist_id) AS assists"
                    " FROM Player"
                    " INNER JOIN Goal ON Goal.assist_id=Player.id"
                    " GROUP BY Player.number, Player.name, Goal.assist_id"
                    " ORDER BY assists DESC;")
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"number":row[0], "name":row[1], "assists":row[2]})

        return response

    @staticmethod
    def list_games():
        stmt = text("SELECT Player.number, Player.name, COUNT(gameplayers.player_id) AS games"
                    " FROM Player"
                    " INNER JOIN gameplayers ON gameplayers.player_id=Player.id"
                    " GROUP BY Player.number, Player.name, gameplayers.player_id"
                    " ORDER BY games DESC;")
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"number":row[0], "name":row[1], "games":row[2]})

        return response

'''
Kehitelmä varatun numeron tunnistamiseen

    @staticmethod
    def list_used_numbers():
        stmt = text("SELECT Player.number FROM Player;")
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"number":row[0]})

        return response
'''