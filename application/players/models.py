from application import db
from application.games.models import Players
from sqlalchemy.sql import text

class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)    
    number = db.Column(db.Integer, nullable=False, unique=True)
    name = db.Column(db.String(48), nullable=False)

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

        