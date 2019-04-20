from application import db
from sqlalchemy.sql import text

# pelaajaa kuvaava luokka
class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)    
    number = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(48), nullable=False)

# liitetään pelaaja tiettyyn käyttäjään mahdollisesti
    #account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
    
    def __init__(self, name, number):
        self.name = name
        self.number = number 

'''
Kehitelmä varatun numeron tunnistamiseen

    @staticmethod
    def list_used_numbers():
        stmt = text("SELECT Player.number FROM Player;")
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"number":row[0]})

        return response
'''