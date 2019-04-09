from application import db
from sqlalchemy.sql import text
from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

class Penalty(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    game_id = db.Column(db.Integer, nullable=False)
    player_id = db.Column(db.Integer, db.ForeignKey('player.id'), nullable=False)
    minutes = db.Column(db.Integer, nullable=False)

    def __init__(self, game_id, player_id, minutes):
        self.game_id = game_id
        self.player_id = player_id
        self.minutes = minutes

