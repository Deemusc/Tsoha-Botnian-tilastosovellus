from application import db

class Goal(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    game_id = db.Column(db.Integer, db.ForeignKey('game.id'), nullable=False)
    scorer_id = db.Column(db.Integer, nullable=False)
    assist_id = db.Column(db.Integer)

    def __init__(self, game_id, scorer_id, assist_id):
        self.game_id = game_id
        self.scorer_id = scorer_id
        self.assist_id = assist_id
    