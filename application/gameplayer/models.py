from application import db

games = db.Table("GamePlayer",
            db.metadata,
            db.Column("game_id", db.Integer, db.ForeignKey("game.id"), primary_key=True),
            db.Column("player_id", db.Integer, db.ForeignKey("player.id"), primary_key=True))

    def __init__(self, game_id, player_id):
        self.game_id = game_id
        self.player_id = player_id