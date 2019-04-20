from application import db
from sqlalchemy.sql import text

'''
# aputaulu monesta-moneen -yhteyttä varten
playerstats = db.Table("playerstats",
            db.metadata,            
            db.Column("player_id", db.Integer, db.ForeignKey("player.id")),
            db.Column("stat_id", db.Integer, db.ForeignKey("stat.id")),
            )
'''

# Varsinainen pelaajaa kuvaava luokka
class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)    
    number = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(48), nullable=False)

# liitetään pelaaja tiettyyn käyttäjään mahdollisesti
    #account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)

# monesta-moneen -yhteys    
   # stats = db.relationship('Stat',
    #        secondary=playerstats, 
     #       back_populates="players")
    
    def __init__(self, name, number):
        self.name = name
        self.number = number 

'''
    @staticmethod
    def list_players():
        stmt = text("SELECT * FROM Player ORDER BY Player.number;")
        res = db.engine.execute(stmt)
        response = []
        for row in res:
            response.append({"id":row[0], "number":row[1], "name":row[2]})
        return response
'''
'''
    @staticmethod
    def list_goal_scorers():
        stmt = text("SELECT Player.number, Player.name, COUNT(Goal.scorer_id) AS goals"
                    " FROM Player"
                    " LEFT JOIN Goal ON Goal.scorer_id=Player.id"
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
                    " LEFT JOIN Goal ON Goal.assist_id=Player.id"
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
                    " LEFT JOIN gameplayers ON gameplayers.player_id=Player.id"
                    " GROUP BY Player.number, Player.name, gameplayers.player_id"
                    " ORDER BY games DESC;")
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"number":row[0], "name":row[1], "games":row[2]})

        return response

    @staticmethod
    def list_penalties():
        stmt = text("SELECT Player.number, Player.name, SUM(Penalty.minutes) AS penalties"
                    " FROM Player"
                    " LEFT JOIN Penalty ON Penalty.player_id=Player.id"
                    " GROUP BY Player.number, Player.name, Penalty.player_id"
                    " ORDER BY penalties DESC;")
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"number":row[0], "name":row[1], "penalties":row[2]})

        return response


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