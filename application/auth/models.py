# tuodaan tarvittavat osat
from application import db
from sqlalchemy.sql import text

# käyttäjää kuvaava luokka
class User(db.Model):

    __tablename__ = "account"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), nullable=False)
    password = db.Column(db.String(32), nullable=False)
    role = db.Column(db.String(10), nullable=False)
    team_id = db.Column(db.Integer, db.ForeignKey('team.id'), nullable=False)

    def __init__(self, username, password, role, team_id):
        self.username = username
        self.password = password
        self.role = role
        self.team_id = team_id

    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

    def roles(self):
        return [self.role]