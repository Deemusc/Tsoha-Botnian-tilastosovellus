from application import db

class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(48), nullable=False)
    number = db.Column(db.Integer)

    def __init__(self, name, number):
        self.name = name
        self.number = number