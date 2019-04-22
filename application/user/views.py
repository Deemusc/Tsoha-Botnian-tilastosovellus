# tuodaan tarvittavat osat
from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user, current_user, login_required

from application import app, db, login_required
from application.auth.models import User
from application.user.forms import UserForm, RegularUserForm

# uuden käyttäjän (roolina 'admin') luominen
@app.route("/user/new", methods=["GET", "POST"])
def user_signup():
    error = None
    form = UserForm()
    if form.validate_on_submit():
        try:
            u = User(teamname=form.teamname.data, username=form.username.data, password=form.password.data, role="ADMIN")            
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
    team = current_user.teamname
    if form.validate_on_submit():
        try:
            u = User(teamname=team, username=form.username.data, password=form.password.data, role="REGULAR")            
            db.session.add(u)
            db.session.commit()
            flash("User created")            
        except Exception as e:
            error = e            
        return redirect(url_for("index"))    
    return render_template("/user/new_regular.html", form = form, error = error) 