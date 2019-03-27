from application import db

class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(48), nullable=False)
    number = db.Column(db.Integer, nullable=False)
    games = db.relationship("Game",
            secondary=games,
            backref=db.backref("players", lazy=True))

    def __init__(self, name, number):
        self.name = name
        self.number = number