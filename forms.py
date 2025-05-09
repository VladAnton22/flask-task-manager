from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired

class AddATask(FlaskForm):
    task_name = StringField("", validators=[InputRequired()], render_kw={"placeholder": "Add a task"})
    submit = SubmitField("Add")