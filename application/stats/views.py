# tuodaan tarvittavat osat
from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application import app, db, login_required
from application.stats.models import Stat
from application.stats.forms import StatForm
from application.games.models import Game
from application.players.models import Player

# lisätään tilastoja tiettyyn peliin, tietylle pelaajalle
@app.route("/stats/<game_id>/", methods=["GET", "POST"])
@login_required(role="ADMIN")
def stats_add(game_id):
    error = None
    form = StatForm(game_id = game_id)
    game = Game.query.filter_by(id=game_id).first_or_404()
    players = Player.query.all()
    players_list = [(p.id, p.name) for p in players]
    form.player_id.choices = players_list

    if form.validate_on_submit():
        try:
            s = Stat(game_id=form.game_id.data, player_id=form.player_id.data, goals=form.goals.data, assists=form.assists.data, penalties=form.penalties.data)
            db.session.add(s)
            db.session.commit()
            flash("statistic added")
        except Exception as e:
            error = e
    return render_template("/stats/add.html", form = form, error = error)

# tilastojen etusivu
@app.route("/stats/", methods=["GET"])
@login_required()
def stats_index():
    p = Stat.list_points()
    
    return render_template("/stats/list.html", points=p)
