from application import db

class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)    
    number = db.Column(db.Integer, nullable=False, primary_key=True, unique=True)
    name = db.Column(db.String(48), nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)

    def __init__(self, name, number):
        self.name = name
        self.number = number