# tuodaan tarvittavat osat
from application import db
from sqlalchemy.sql import text

# pelaajaa kuvaava luokka
class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)    
    number = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(48), nullable=False)

    team_id = db.Column(db.Integer, db.ForeignKey('team.id'), nullable=False)
    
    def __init__(self, name, number):
        self.name = name
        self.number = number      

# metodi, joka antaa tiettyyn peliin jo lisätyt pelaajat
    @staticmethod
    def players_in_game(id):
        stmt = text("SELECT Player.id, Player.number, Player.name"
                    " FROM PLAYER"
                    " INNER JOIN Stat ON Stat.player_id=Player.id"
                    " WHERE Stat.game_id = :id;").params(id=id)
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"id":row[0], "number":row[1], "name":row[2]})

        return response    

# metodi, joka antaa kaikki pelaajat
    @staticmethod
    def list_all(team_id):
        stmt = text("SELECT Player.id, Player.number, Player.name"
                    " FROM PLAYER" 
                    " WHERE Player.team_id = :team_id;").params(team_id=team_id)
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"id":row[0], "number":row[1], "name":row[2]})

        return response 