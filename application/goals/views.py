from flask import redirect, render_template, request, url_for
from flask_login import login_required

from application import app, db
from application.goals.models import Goal
from application.goals.forms import GoalForm

#@app.route("/goals/", methods=["GET", "POST"])
#@login_required
#def goals_add(game_id):
#    error = None
#    form = GoalForm()
#    if form.validate_on_submit():
#        try:
#            g = Goal(game_id=game_id, scorer_id)


