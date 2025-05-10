from flask import Blueprint, render_template, redirect, flash, url_for, request, session
from ..forms import LoginForm, RegistrationForm
from ..models import User
from app import db
from sqlalchemy import select
from flask_login import login_user, logout_user, login_required, current_user

auth_bp = Blueprint('auth', __name__)

@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        stmt = select(User).where(User.name == form.name.data)
        existing_user = db.session.scalars(stmt).one_or_none()
        if existing_user:
            form.name.errors.append("Username already taken.")
        else:
            user = User(name=form.name.data)
            user.set_password(form.password.data)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for("auth.login"))

    return render_template("register.html", form=form)

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        stmt = select(User).where(User.name == form.name.data)
        user = db.session.scalars(stmt).one_or_none()
        if user and user.check_password(form.password.data):
            login_user(user)
            return redirect(url_for("task.index"))
        else:
            flash("Invalid username or password.", "error")
    return render_template("login.html", form=form)

from flask_login import logout_user
@auth_bp.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth.login"))



#-----DELETE USER------
# @auth_bp.route("/delete_user/<username>", methods=["GET"])
# def delete_user(username):
#     stmt = select(User).where(User.name == username)
#     users = db.session.scalars(stmt).all()

#     if not users:
#         flash("User not found.", "error")
#     else:
#         for user in users:
#             db.session.delete(user)
#         db.session.commit()
#         flash(f"Deleted {len(users)} user(s) with the name '{username}'.", "success")

#     return redirect(url_for("auth.register"))  # or any appropriate page