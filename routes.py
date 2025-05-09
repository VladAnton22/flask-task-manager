from flask import render_template, request
# from models import User
from forms import AddATask

def register_routes(app, db):

    @app.route('/')
    def index():
        form = AddATask()
        task_name = form.task_name.data
        return render_template("index.html", form=form)