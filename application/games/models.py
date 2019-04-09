from application import db

class Players(object):
    # Luokkaa käytetään aputaululle, jolla liitetään ottelut ja pelaajat monesta moneen -yhteydellä
    def __init__(self, player_id, game_id):
        self.player_id = player_id
        self.game_id = game_id

# aputaulu
players = db.Table("players",
            db.metadata,
            db.Column("id", db.Integer, primary_key = True),
            db.Column("player_id", db.Integer, db.ForeignKey("player.id")),
            db.Column("game_id", db.Integer, db.ForeignKey("game.id")),
            )
# uniikki indeksi player_id:lle ja game_id:lle
db.Index("roster", players.c.game_id, players.c.player_id, unique = True)

class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    opponent = db.Column(db.String(32), nullable=False)
    botnia_goals = db.Column(db.Integer, nullable=False)
    opponent_goals = db.Column(db.Integer, nullable=False)

    players = db.relationship('Player',
                secondary=players, 
                backref=db.backref("games", lazy="dynamic"),
                )

    def __init__(self, date, opponent, botnia_goals, opponent_goals):
        self.date = date
        self.opponent = opponent
        self.botnia_goals = botnia_goals
        self.opponent_goals = opponent_goals
