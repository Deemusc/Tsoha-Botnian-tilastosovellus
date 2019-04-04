from application import db
from sqlalchemy.sql import text

class Goal(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    game_id = db.Column(db.Integer, db.ForeignKey('game.id'), nullable=False)
    scorer_id = db.Column(db.Integer, nullable=False)
    assist_id = db.Column(db.Integer, nullable=False)

    def __init__(self, game_id, scorer_id, assist_id):
        self.game_id = game_id
        self.scorer_id = scorer_id
        self.assist_id = assist_id
    
    @staticmethod
    def find_amount_of_goals_in_game(game_id):
        stmt = text("SELECT COUNT(game_id) FROM Goal"
                    " WHERE game_id=:id")
        stmt = stmt.bindparams(id=game_id)
        res = db.engine.execute(stmt)
        
        for row in res:
            response = row[0]

        return response   