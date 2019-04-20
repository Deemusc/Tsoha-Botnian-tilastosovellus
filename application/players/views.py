# tuodaan tarvittavat osat
from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application import app, db, login_required
from application.players.models import Player
from application.players.forms import PlayerForm, queryForm

# uuden pelaajan luominen, lisää pelaajan tietokantaan, vaatii adminin
@app.route("/players/new/", methods=["GET", "POST"])
@login_required(role="ADMIN")
def players_create():
    error = None
    form = PlayerForm()
    if form.validate_on_submit():
        try:
            p = Player(number=form.number.data, name=form.name.data)
            db.session.add(p)
            db.session.commit()
            flash("Player added")            
        except Exception as e:
            error = e          
        return redirect(url_for("players_index"))    
    return render_template("/players/new.html", form = form, error = error)

# pelaajien listaus, hakee kaikki tiedot taulusta player
@app.route("/players/", methods=["GET"])
@login_required()
def players_index():
    p = Player.query.all()
    return render_template("/players/list.html", players=p)

# pelaajien haku, suorittaa kyselyn pelaajan nimen osalla
@app.route("/players/query/", methods=["GET", "POST"])
@login_required()
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

# pelaajan muokkaaminen, hakee pelaajan id:n perusteella ja päivittää sen tietoja, vaatii adminin
@app.route("/players/edit/<int:id>/", methods=["GET", "POST"])
@login_required(role="ADMIN")
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

# pelaajan poistaminen, hakee pelajaan id:n perusteella ja poistaa tietokannasta, vaatii adminin
@app.route("/players/delete/<int:id>/", methods=["GET", "POST"])
@login_required(role="ADMIN")
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
    