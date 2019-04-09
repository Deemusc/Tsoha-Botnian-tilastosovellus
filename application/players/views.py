from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application import app, db, login_required
from application.players.models import Player
from application.players.forms import PlayerForm, queryForm
from application.games.models import Players

# Pelaajien listaus. Tavallinen käyttäjä voi tarkastella listaa.
@app.route("/players/", methods=["GET"])
@login_required(role="REGULAR")
def players_index():
    p = Player.query.all()
    return render_template("/players/list.html", players=p)

# Maalipörssi. Listataan järjestyksessä kaikki pelaajat, jotka ovat tehneet maaleja.
@app.route("/players/scorers/", methods=["GET"])
@login_required(role="REGULAR")
def players_scorers():
    s = Player.list_goal_scorers()
    return render_template("/players/scorers.html", scorers=s)

# Pelaajien haku-sivu, toimii mukavasti.
@app.route("/players/query/", methods=["GET", "POST"])
@login_required(role="REGULAR")
def players_query():
    error = None
    form = queryForm()
    if form.validate_on_submit():
        n = form.name.data + "%"  
        p = Player.query.filter(Player.name.like(n)).all()        
        if p:
            return render_template("/players/query.html", form=form, players=p)
        else:
            error = "No players"
    return render_template("/players/query.html", form=form, error=error)

# Uuden pelaajan luominen, siirtää käyttäjän pelaajien listaukseen.
@app.route("/players/new/", methods=["GET", "POST"])
@login_required(role="REGULAR")
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
        return redirect(url_for("players_index"))    
    return render_template("/players/new.html", form = form, error = error)   

# Pelaajan muokkaaminen, siirtää käyttäjän pelaajien listaukseen.
@app.route("/players/edit/<int:id>/", methods=["GET", "POST"])
@login_required(role="REGULAR")
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
        return redirect(url_for("players_index"))    
    return render_template("/players/edit.html", form = form, error=error)

# Pelaajan poistaminen.
@app.route("/players/delete/<int:id>/", methods=["GET", "POST"])
@login_required(role="REGULAR")
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
        return redirect(url_for("players_index"))    
    return render_template("/players/list.html", error=error)
