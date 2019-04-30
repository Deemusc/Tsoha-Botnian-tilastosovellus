# tuodaan tarvittavat osat
from flask import redirect, render_template, request, url_for, flash
from flask_login import login_required, current_user

from application import app, db, login_required
from application.games.models import Game
from application.games.forms import GameForm, queryGameForm
from application.stats.models import Stat
from application.teams.models import Team

# Uuden pelin luominen, vaatii adminin
@app.route("/games/new/", methods=["GET", "POST"])
@login_required(role="ADMIN")
def games_create():
    error = None
    form = GameForm()
    if form.validate_on_submit():
        try:
            g = Game(date=form.date.data, opponent=form.opponent.data, our_goals=form.our_goals.data, opponent_goals=form.opponent_goals.data)
            g.team_id = current_user.team_id
            db.session.add(g)            
            db.session.commit()
            flash("game added")
        except Exception as e:
            error = e 
        # siirrytään pelin tilastojen syöttämiseen
        return redirect(url_for("stats_add", game_id = g.id))
    return render_template("/games/new.html", form = form, error = error)  

#pelien listaus
@app.route("/games/", methods=["GET"])
@login_required()
def games_index():
    g = Game.query.filter(Game.team_id == current_user.team_id).all()
    return render_template("/games/list.html", games=g)

# pelien hakutoiminto, atm vain vastustajan nimellä
@app.route("/games/query/", methods=["GET", "POST"])
@login_required()
def games_query():
    error = None
    form = queryGameForm()
    if form.validate_on_submit():
        n = form.opponent.data + "%" 
        g = Game.query.filter(Game.team_id == current_user.team_id, Game.opponent.like(n)).all()
        if g:
            return render_template("/games/query.html", form=form, games=g)
        else:
            error = "No games"
    return render_template("/games/query.html", form=form, error=error)

# Pelin muokkaaminen, vaatii adminin
@app.route("/games/edit/<int:id>/", methods=["GET", "POST"])
@login_required(role="ADMIN")
def games_edit(id):
    error = None
    g = Game.query.filter_by(id=id).first_or_404()
    if g.team_id != current_user.team_id:
        flash("You can only edit your own team data.")
        return redirect(url_for("games_index"))
    form = GameForm(obj=g)
    if form.validate_on_submit():
        try:
            g.date = form.date.data
            g.opponent = form.opponent.data
            g.our_goals = form.our_goals.data
            g.opponent_goals = form.opponent_goals.data
            db.session.commit()
            flash("Game info updated")
        except Exception as e:
            error = e
        return redirect(url_for("games_index"))
    return render_template("/games/edit.html", form = form, error=error)

# pelin yksityiskohdat
@app.route("/games/details/<int:id>/", methods=["GET", "POST"])
@login_required()
def games_details(id):
    error = None
    g = Game.query.filter_by(id=id).first_or_404()
    s = Stat.game_details(id)

    return render_template("/games/details.html/", game=g, stats=s)

# Pelin poistaminen, vaatii adminin
@app.route("/games/delete/<int:id>/", methods=["GET", "POST"])
@login_required(role="ADMIN")
def games_delete(id):
    error = None
    g = Game.query.filter_by(id=id).first_or_404()
    if g.team_id != current_user.team_id:
        flash("You can only edit your own team data.")
        return redirect(url_for("games_index"))
    if g:
        try:
            db.session.delete(g)
            Stat.delete_stats(g.id)
            db.session.commit()
            flash("Game deleted")
        except Exception as e:
            error = e
        return redirect(url_for("games_index"))
    return render_template("/games/list.html", error=error)
