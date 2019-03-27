from flask import redirect, render_template, request, url_for
from flask_login import login_required

from application import app, db
from application.games.models import Game
from application.games.forms import GameForm

@app.route("/games/", methods=["GET"])
def games_index():
    return render_template("games/list.html", games = Game.query.all())

@app.route("/games/new/")
#@login_required
def games_form():
    return render_template("games/new.html", form = GameForm())

#@app.route("/games/edit/")
#@login_required
#def games_editForm():
#    return render_template("games/edit.html", form = GameEditForm())

@app.route("/games/<game_id>/", methods=["POST"])
#@login_required
def games_set_botnia_goals(game_id):

    g = Game.query.get(game_id)
    g.botnia_goals = request.form.get("botnia_goals")
    db.session.commit()

    return redirect(url_for("games_index"))    

#@app.route("/games/", methods=["GET", "POST"])
#@login_required
#def games_edit():
#    form = GameEditForm(request.form)
#
#    if not form.validate():
#        return render_template("games/edit.html", form = form)
#
#    g = Game.query.get(form.id.data)
#    
#    g.date = form.date.data
#    g.opponent = form.opponent.data
#   g.botnia_goals = form.botnia_goals.data
#    g.opponent_goals = form.opponent_goals.data
#
#   db.session.merge(g)
#    db.session.flush()
#    db.session().commit()
#
#    return redirect(url_for("games_index"))

@app.route("/games/", methods=["POST"])
#@login_required
def games_create():
    form = GameForm(request.form)

    if not form.validate():
        return render_template("games/new.html", form = form)

    g = Game(form.date.data, form.opponent.data, form.botnia_goals.data, form.opponent_goals.data)
    
    db.session().add(g)
    db.session().commit()

    return redirect(url_for("games_index"))

