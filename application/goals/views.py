from flask import redirect, render_template, request, url_for
from flask_login import login_required

from application import app, db
from application.goals.models import Goal
from application.goals.forms import GoalForm
from application.games.models import Game



@app.route("/goals/<game_id>", methods=["GET", "POST"])
#@login_required
def goals_add(game_id):
    error = None
    form = GoalForm()
    return render_template("/goals/add.html", form = form, error = error) 

@app.route("/goals/new/", methods=["GET", "POST"])
#@login_required
def goals_create():
    error = None
    form = GoalForm()
    print('form:', form)
    if form.validate_on_submit():
        try:
            s = Player.query.filter_by(number=form.scorer_number.data).first_or_404()
            a = Player.query.filter_by(number=form.assist_number.data).first_or_404()
            g = Goal(game_id=form.id.data, scorer_id=s.id, assist_id=a.id)
            print('tietoja:', s.id, a.id, g)
            db.session.add(g)
            db.session.commit()
            flash("goal added")
        except Exception as e:
            error = e
    return render_template("/goals/add.html", form = form, error = error)