from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application import app, db
from application.players.models import Player
from application.players.forms import PlayerForm, queryForm

# Pelaajien listaus.
@app.route("/players/", methods=["GET"])
def players_index():
    p = Player.query.all()
    return render_template("/players/list.html", players=p)

# Pelaajien haku-sivu, toimii mukavasti.
@app.route("/players/query/", methods=["GET", "POST"])
@login_required
def players_query():
    error = None
    form = queryForm()
    if form.validate_on_submit():
        p = Player.query.filter_by(name=form.name.data).all()
        if p:
            return render_template("/players/query.html", form=form, players=p)
        else:
            error = "No players"
    return render_template("/players/query.html", form=form, error=error)

# Uuden pelaajan luominen, ei siirrä käyttäjää (vielä) pelaajien listaukseen.
@app.route("/players/new/", methods=["GET", "POST"])
@login_required
def players_create():
    error = None
    form = PlayerForm()
    if form.validate_on_submit():
        try:
            p = Player(number=form.number.data, name=form.name.data)
            p.account_id = current_user.id
            db.session.add(p)
            db.session.commit()
            flash("Player added")
        except Exception as e:
            error = e            
    return render_template("/players/new.html", form = form, error = error)   

# Pelaajan muokkaaminen, ei siirrä käyttäjää (vielä) pelaajien listaukseen.
@app.route("/players/edit/<int:id>/", methods=["GET", "POST"])
@login_required
def players_edit(id):
    error = None
    p = Player.query.filter_by(id=id).first_or_404()
    form = PlayerForm(obj=p)
    if form.validate_on_submit():
        try:
            p.number = form.number.data
            p.name = form.name.data
            db.session.commit()
            flash("Player's info updated")
        except Exception as e:
            error = e
    return render_template("/players/edit.html", form = form, error=error)

# Pelaajan poistaminen, ei siirrä käyttäjää (vielä) pelaajien listaukseen.
@app.route("/players/delete/<int:id>/", methods=["GET", "POST"])
@login_required
def players_delete(id):
    error = None
    p = Player.query.filter_by(id=id).first_or_404()
    if p:
        try:
            db.session.delete(p)
            db.session.commit()
            flash("Player deleted")
        except Exception as e:
            error = e
    return render_template("/players/list.html", error=error)
