from flask import Blueprint, render_template, redirect, flash, url_for, request, session
from ..forms import LoginForm, RegistrationForm
from ..models import User
from app import db
from sqlalchemy import select

auth_bp = Blueprint('auth', __name__)

@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        stmt = select(User).where(User.name == form.name.data)
        existing_user = db.session.execute(stmt).scalar_one_or_none()
        if existing_user:
            form.name.errors.append("Username already taken.")
            return redirect(url_for("auth.register"))

        user = User(name=form.name.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("Registration successful! Please log in.", "success")
        return redirect(url_for("auth.login"))

    return render_template("register.html", form=form)

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    
    return render_template("login.html", form=form)