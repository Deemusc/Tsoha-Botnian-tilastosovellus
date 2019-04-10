from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application import app, db, login_required
from application.games.models import Game
from application.games.forms import GameForm, queryGameForm
from application.goals.models import Goal
from application.goals.forms import GoalForm
from application.goals.views import goals_add
from application.players.forms import addToGameForm
from application.players.models import Player


#pelien listaus
@app.route("/games/", methods=["GET"])
@login_required()
def games_index():
    g = Game.query.all()
    return render_template("/games/list.html", games=g)

# pelien hakutoiminto, atm vain vastustajan nimellä
@app.route("/games/query/", methods=["GET", "POST"])
@login_required()
def games_query():
    error = None
    form = queryGameForm()
    if form.validate_on_submit():
        n = form.opponent.data + "%" 
        g = Game.query.filter(Game.opponent.like(n)).all()
        if g:
            return render_template("/games/query.html", form=form, games=g)
        else:
            error = "No games"
    return render_template("/games/query.html", form=form, error=error)

# Uuden pelin luominen.
@app.route("/games/new/", methods=["GET", "POST"])
@login_required(role="ADMIN")
def games_create():
    error = None
    form = GameForm()
    if form.validate_on_submit():
        try:
            g = Game(date=form.date.data, opponent=form.opponent.data, botnia_goals=0, opponent_goals=form.opponent_goals.data)
            db.session.add(g)            
            db.session.commit()
            flash("game added")
        except Exception as e:
            error = e 
        # Pelin luominen jatkuu maalien yksityiskohtien syöttämisellä.
        return redirect(url_for("games_roster", game_id = g.id))
    return render_template("/games/new.html", form = form, error = error)   

# Pelaajien lisääminen tiettyyn peliin.
@app.route("/games/roster/<game_id>", methods=["GET", "POST"])
@login_required(role="ADMIN")
def games_roster(game_id):
    error = None
    form = addToGameForm(game_id = game_id)
    game = Game.query.filter_by(id=game_id).first_or_404()
    p = Player.query.all()
    
    if form.validate_on_submit():
        try:
            player = Player.query.filter_by(number=form.player_number.data).first_or_404()                        
            game.players.append(player)
            db.session.add(game)
            db.session.commit()
            flash("player added")
        except Exception as e:
            error = e
    return render_template("/games/roster.html", form = form, error = error, players = p)

'''
@app.route("/games/roster/add/<game_id>", methods=["GET", "POST"])
@login_required(role="ADMIN")
def games_roster_finish(game_id, players):
    game = Game.query.filter_by(id=game_id).first_or_404()
    game.players.append(players)
    db.session.commit()
    return redirect(url_for("goals_add", game_id = game.id))
'''

# Pelin muokkaaminen
@app.route("/games/edit/<int:id>/", methods=["GET", "POST"])
@login_required(role="ADMIN")
def games_edit(id):
    error = None
    g = Game.query.filter_by(id=id).first_or_404()
    form = GameForm(obj=g)
    if form.validate_on_submit():
        try:
            g.date = form.date.data
            g.opponent = form.opponent.data
            g.opponent_goals = form.opponent_goals.data
            db.session.commit()
            flash("Game info updated")
        except Exception as e:
            error = e
        return redirect(url_for("games_index"))
    return render_template("/games/edit.html", form = form, error=error)

# Pelin poistaminen
@app.route("/games/delete/<int:id>/", methods=["GET", "POST"])
@login_required(role="ADMIN")
def games_delete(id):
    error = None
    g = Game.query.filter_by(id=id).first_or_404()
    if g:
        try:
            db.session.delete(g)
            db.session.commit()
            flash("Game deleted")
        except Exception as e:
            error = e
        return redirect(url_for("games_index"))
    return render_template("/games/list.html", error=error)
