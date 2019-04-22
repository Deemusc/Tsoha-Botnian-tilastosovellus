# tuodaan tarvittavat osat
from application import db
from application.models import Base
from sqlalchemy.sql import text

# käyttäjää kuvaava luokka
class User(Base):

    __tablename__ = "account"

    teamname = db.Column(db.String(48), nullable=False)
    username = db.Column(db.String(32), nullable=False)
    password = db.Column(db.String(32), nullable=False)
    role = db.Column(db.String(10), nullable=False)

    def __init__(self, teamname, username, password, role):
        self.teamname = teamname
        self.username = username
        self.password = password
        self.role = role

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