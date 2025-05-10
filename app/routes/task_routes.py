from flask import Blueprint, render_template
from ..forms import AddATask  # relative import

task_bp = Blueprint('task', __name__)

@task_bp.route('/')
def index():
    form = AddATask()
    task_name = form.task_name.data
    return render_template("index.html", form=form)
