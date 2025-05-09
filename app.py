from flask import Flask, render_template, session
from flask_session import Session
from forms import AddATask

app = Flask(__name__)
app.config["SECRET_KEY"] = "this-is-my-secret-key"
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/", methods=["GET", "POST"])
def index():
    form = AddATask()
    task_name = form.task_name.data
    return render_template("index.html", form=form)

