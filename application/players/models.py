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
        stmt = text("SELECT number, name, COUNT(scorer_id) FROM Player"
                    " JOIN Goal ON scorer_id=player.id;")
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"name":row[1], "goals":row[2]})

        return response