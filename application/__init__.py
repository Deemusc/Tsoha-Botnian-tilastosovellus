# Flask tuodaan käyttöön
from flask import Flask
app = Flask(__name__)

# SQLAlchemy mukaan
from flask_sqlalchemy import SQLAlchemy
# Käytetään players.db -nimistä SQLite-tietokantaa. Kolme vinoviivaa
# = tiedosto sijaitsee sovelluksen tiedostojen kanssa samassa paikassa
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///players.db"

# SQLAlchemy tulostaa kaikki SQL-kyselyt
app.config["SQLALCHEMY_ECHO"] = True

# Luodaan db-olio, jota käytetään tietokannan käsittelyyn
db = SQLAlchemy(app)

# Luetaan kansiosta application tiedoston views sisältö
from application import views

# Tuodaan luokat models ja views käyttöön
from application.players import models
from application.players import views

# Luodaan tarvittavat tietokantataulut
db.create_all()