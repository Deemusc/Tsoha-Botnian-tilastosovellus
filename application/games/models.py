from application import db

class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date = db.Column(db.Date, nullable=False)
    opponent = db.Column(db.String(32), nullable=False)
    botnia_goals = db.Column(db.Integer, nullable=False)
    opponent_goals = db.Column(db.Integer, nullable=False)

    def __init__(self, date, opponent, botnia_goals, opponent_goals):
        self.date = date
        self.opponent = opponent
        self.botnia_goals = botnia_goals
        self.opponent_goals = opponent_goals
        