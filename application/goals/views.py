from flask import redirect, render_template, request, url_for
from flask_login import login_required

from application import app, db
from application.goals.models import Goal
from application.goals.forms import GoalForm
from application.games.models import Game
from application.players.models import Player



@app.route("/goals/<game_id>", methods=["GET", "POST"])
#@login_required
def goals_add(game_id):
    error = None
    form = GoalForm(game_id = game_id)
    print('form:', form)
    if form.validate_on_submit():
        try:
            s = Player.query.filter_by(number=form.scorer_number.data).first_or_404()
            a = Player.query.filter_by(number=form.assist_number.data).first_or_404()
            g = Goal(game_id=game_id, scorer_id=s.id, assist_id=a.id)
            print('tietoja:', g)
            db.session.add(g)
            db.session.commit()
            flash("goal added")
        except Exception as e:
            error = e
    return render_template("/goals/add.html", form = form, error = error)
    #return redirect(url_for("goals_create", game_id = game_id)) 


# ---------- tätä ei juuri nyt tarvita --------
@app.route("/goals/<game_id>", methods=["GET", "POST"])
#@login_required
def goals_create(game_id):
    error = None
    form = GoalForm()
    print('form:', form)
    if form.validate_on_submit():
        try:
            s = Player.query.filter_by(number=form.scorer_number.data).first_or_404()
            a = Player.query.filter_by(number=form.assist_number.data).first_or_404()
            g = Goal(game_id=game_id, scorer_id=s.id, assist_id=a.id)
            print('tietoja:', g)
            db.session.add(g)
            db.session.commit()
            flash("goal added")
        except Exception as e:
            error = e
    return render_template("/goals/add.html", form = form, error = error)