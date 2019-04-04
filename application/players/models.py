from application import db
from sqlalchemy.sql import text

class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)    
    number = db.Column(db.Integer, nullable=False, unique=True)
    name = db.Column(db.String(48), nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)

    def __init__(self, name, number):
        self.name = name
        self.number = number

    @staticmethod
    def list_goal_scorers():
        stmt = text("SELECT number, name, COUNT(scorer_id) as goals FROM Player"
                    " JOIN Goal ON scorer_id=player.id"
                    " GROUP BY scorer_id ORDER BY goals DESC;")
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"number":row[0], "name":row[1], "goals":row[2]})

        return response