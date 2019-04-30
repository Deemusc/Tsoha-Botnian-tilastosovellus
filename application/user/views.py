# tuodaan tarvittavat osat
from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, current_user, login_required

from application import app, db, login_required
from application.auth.models import User
from application.teams.models import Team
from application.user.forms import UserForm, RegularUserForm

# uuden käyttäjän (roolina 'admin') luominen
@app.route("/user/new/<team_id>", methods=["GET", "POST"])
def user_signup(team_id):
    error = None
    form = UserForm(team_id=team_id)
    if form.validate_on_submit():
        try:
            u = User(username=form.username.data, password=form.password.data, role="ADMIN", team_id=team_id)       
            db.session.add(u)
            db.session.commit()
            flash("User created")            
        except Exception as e:
            error = e            
        return redirect(url_for("auth_login"))    
    return render_template("/user/new.html", form = form, error = error)   

# uuden peruskäyttäjän luominen joukkueelle
@app.route("/user/new_regular", methods=["GET", "POST"])
@login_required(role="ADMIN")
def regular_user_signup():
    error = None
    form = RegularUserForm()
    team = current_user.team_id
    if form.validate_on_submit():
        try:
            u = User(username=form.username.data, password=form.password.data, role="REGULAR", team_id = team)            
            db.session.add(u)
            db.session.commit()
            flash("User created")            
        except Exception as e:
            error = e            
        return redirect(url_for("index"))    
    return render_template("/user/new_regular.html", form = form, error = error)