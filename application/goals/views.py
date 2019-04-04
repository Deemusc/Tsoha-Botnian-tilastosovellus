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
    game = Game.query.filter_by(id=game_id).first_or_404()
    #goalsToAdd = game.botnia_goals

    if form.validate_on_submit():
        try:
            s = Player.query.filter_by(number=form.scorer_number.data).first_or_404()
            a = Player.query.filter_by(number=form.assist_number.data).first_or_404()
            g = Goal(game_id=game_id, scorer_id=s.id, assist_id=a.id)
            db.session.add(g)
            db.session.commit()
            flash("goal added")
        except Exception as e:
            error = e
    return render_template("/goals/add.html", form = form, error = error)

@app.route("/goals/add/<game_id>", methods=["GET", "POST"])
#@login required
def goals_finish(game_id):
    error = None
    #print('lollero')
    game = Game.query.filter_by(id=game_id).first_or_404()
    goals_in_game = Goal.find_amount_of_goals_in_game(game_id)
    print(goals_in_game)
    game.botnia_goals = goals_in_game
    db.session.commit()


    return redirect(url_for("games_index"))    
    
    
    

# ---------- tätä ei juuri nyt tarvita --------
#@app.route("/goals/<game_id>", methods=["GET", "POST"])
#@login_required
#def goals_create(game_id):
#    game = Game.query.filter_by(id=game_id).first_or_404()
#    goalsToAdd = game.botnia_goals

