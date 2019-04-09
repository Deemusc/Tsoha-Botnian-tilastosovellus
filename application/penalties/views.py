from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application import app, db, login_required
from application.goals.models import Goal
from application.goals.forms import GoalForm
from application.games.models import Game
from application.players.models import Player
from application.penalties.models import Penalty
from application.penalties.forms import PenaltyForm
from application.games.forms import GameForm
from application.players.forms import PlayerForm


@app.route("/penalties/<game_id>/", methods=["GET", "POST"])
@login_required(role="REGULAR")
def penalties_add(game_id):
    error = None
    form = PenaltyForm(game_id = game_id)
    game = Game.query.filter_by(id=game_id).first_or_404()

    if form.validate_on_submit():
        try:
            p = Player.query.filter_by(number=form.player_number.data).first_or_404()            
            penalty = Penalty(game_id=game_id, player_id=p.id, minutes=form.minutes.data)            
            db.session.add(penalty)
            db.session.commit()
            flash("penalty added")
        except Exception as e:
            error = e
    return render_template("/penalties/add.html", form = form, error = error)

