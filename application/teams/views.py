# tuodaan tarvittavat osat
from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user, current_user, login_required

from application import app, db, login_required
from application.auth.models import User
from application.teams.models import Team
from application.teams.forms import TeamForm

# uuden käyttäjän (roolina 'admin') luominen
@app.route("/teams/new", methods=["GET", "POST"])
def team_signup():
    error = None
    form = TeamForm()
    if form.validate_on_submit():
        try:
            t = Team(name=form.name.data)       
            db.session.add(t)
            db.session.commit()
            flash("Team created")            
        except Exception as e:
            error = e            
        return redirect(url_for("user_signup", team_id = t.id))    
    return render_template("/teams/new.html", form = form, error = error)  