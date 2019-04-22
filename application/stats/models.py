# tuodaan tarvittavat osat
from application import db
from sqlalchemy.sql import text

# tilastotaulua kuvaava luokka
class Stat(db.Model):
    # varmistetaan, ettei tietokantaan mene samalle pelaajalle yhteen otteluun useampia tilastoja
    __table_args__ = (
        db.UniqueConstraint("game_id", "player_id", name="unique_game_player"),
    )
    id = db.Column(db.Integer, primary_key=True)
    game_id = db.Column(db.Integer, db.ForeignKey("game.id"), nullable=False)
    player_id = db.Column(db.Integer, db.ForeignKey("player.id"), nullable=False)    
    goals = db.Column(db.Integer, nullable=False)
    assists = db.Column(db.Integer, nullable=False)
    penalties = db.Column(db.Integer, nullable=False)

    def __init__(self, game_id, player_id, goals, assists, penalties):
        self.game_id = game_id
        self.player_id = player_id
        self.goals = goals
        self.assists = assists
        self.penalties = penalties
        
# metodi tilastojen hakemiseen
    @staticmethod
    def list_points(teamname):
        stmt = text("SELECT Player.number, Player.name, COUNT(Stat.player_id) AS games,"
                    " SUM(Stat.goals) AS goals,"
                    " SUM(Stat.assists) AS assists, SUM(goals + assists) AS points,"
                    " SUM(Stat.penalties) AS penalties"
                    " FROM Player"
                    " LEFT JOIN Stat ON Stat.player_id=Player.id"
                    " WHERE Player.teamname = :teamname"
                    " GROUP BY Player.id"
                    " ORDER BY points DESC, goals DESC, penalties;").params(teamname="'" + teamname + "'")
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

# metodi tietyn pelin tilastojen hakemiseen
    @staticmethod
    def game_details(id):
        stmt = text("SELECT Player.number, Player.name, Stat.goals, Stat.assists, Stat.penalties"
                    " FROM Player INNER JOIN Stat ON Stat.player_id=Player.id"
                    " WHERE Stat.game_id = :id;").params(id=id)
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"number":row[0], "name":row[1], "goals":row[2], "assists":row[3], "penalties":row[4]})

        return response