# tuodaan tarvittavat osat
from application import db
from sqlalchemy.sql import text

# tilastotaulua kuvaava luokka
class Stat(db.Model):
    __table_args__ = (
        db.UniqueConstraint("game_id", "player_id", name="unique_game_player"),
    )
    id = db.Column(db.Integer, primary_key=True, auto_increment=True)
    game_id = db.Column(db.Integer, db.ForeignKey("game.id"), nullable=False)
    player_id = db.Column(db.Integer, db.ForeignKey("player.id"), nullable=False)    
    goals = db.Column(db.Integer, nullable=False)
    assists = db.Column(db.Integer, nullable=False)
    penalties = db.Column(db.Integer, nullable=False)

# monesta-moneen -yhteys pelaajiin
    #players = db.relationship('Player',
     #           secondary=playerstats, 
      #          back_populates="stats")

# monesta-moneen -yhteys otteluihin
    #games = db.relationship("Game",
     #       secondary=gamestats,
      #      back_populates="stats")

    def __init__(self, game_id, player_id, goals, assists, penalties):
        self.game_id = game_id
        self.player_id = player_id
        self.goals = goals
        self.assists = assists
        self.penalties = penalties
        
# metodi tilastojen hakemiseen
    @staticmethod
    def list_points():
        stmt = text("SELECT Player.number, Player.name, COUNT(Stat.player_id) AS games,"
                    " SUM(Stat.goals) AS goals,"
                    " SUM(Stat.assists) AS assists, SUM(goals + assists) AS points,"
                    " SUM(Stat.penalties) AS penalties"
                    " FROM Player"
                    " LEFT JOIN Stat ON Stat.player_id=Player.id"
                    " GROUP BY Player.id"
                    " ORDER BY points DESC, goals DESC, penalties;")
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"number":row[0], "name":row[1], "games":row[2], "goals":row[3], "assists":row[4], "points":row[5], "penalties":row[6]})

        return response

# metodi tilastojen poistamiseen, kun peli poistetaan
    @staticmethod
    def delete_stats(game_id):
        stmt = text("DELETE FROM Stat WHERE game_id = :game_id;").params(game_id=game_id)
        res = db.engine.execute(stmt)