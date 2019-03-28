from application import db

class Goal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    game_id = db.Column(db.Integer, db.ForeignKey('game.id'), nullable=False)
    scorer_id = db.Column(db.Integer, nullable=False)
    assist_id = db.Column(db.Integer)

    def __init__(self, game_id):
        self.game_id
        self.scorer_id
        
    