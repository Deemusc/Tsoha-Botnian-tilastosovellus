from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user

from application import app, db
from application.auth.models import User
from application.user.forms import UserForm

@app.route("/user/new", methods=["GET", "POST"])
def user_signup():
    form = UserForm()

    u = User(form.name.data, form.username.data, form.password.data)

    error = None
    form = UserForm()
    if form.validate_on_submit():
        try:
            u = User(name=form.name.data, username=form.username.data, password=form.password.data)            
            db.session.add(u)
            db.session.commit()
            flash("User created")            
        except Exception as e:
            error = e            
        return redirect(url_for("players_index"))    
    return render_template("/user/new.html", form = form, error = error)   