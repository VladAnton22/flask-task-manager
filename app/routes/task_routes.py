from flask import Blueprint, render_template, redirect, url_for, session
from ..forms import AddATask  # relative import
from flask_login import current_user, login_required
from ..models import Task, User
from app import db
from sqlalchemy import select

task_bp = Blueprint('task', __name__)

@task_bp.route('/')
def index():
    return render_template("index.html")

@task_bp.route('/tasks', methods=["GET", "POST"])
@login_required
def task_management():
    form = AddATask()
    if form.validate_on_submit():
        new_task = Task(
            title=form.title.data,
            description=form.description.data,
            due_date=form.due_date.data,
            priority=int(form.priority.data),
            status=form.status.data,
            user_id=current_user.id
        )
        db.session.add(new_task)
        db.session.commit()
        return redirect(url_for("task.index"))
    
    stmt = select(Task).join(Task.user).where(User.name == current_user.name)
    tasks = db.session.scalars(stmt).all()

    return render_template("task_management.html", form=form, tasks=tasks)
