from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import InputRequired, EqualTo

class AddATask(FlaskForm):
    task_name = StringField("", validators=[InputRequired()], render_kw={"placeholder": "Add a task"})
    submit = SubmitField("Add")

class RegistrationForm(FlaskForm):
    name = StringField("Username", validators=[InputRequired()])
    password = PasswordField("Password", validators=[InputRequired()])
    password2 = PasswordField("Repeat Password", validators=[InputRequired(), EqualTo("password")])
    submit = SubmitField("Register")

class LoginForm(FlaskForm):
    name = StringField("Username", validators=[InputRequired()])
    password = PasswordField("Password", validators=[InputRequired()])
    submit = SubmitField("Log in")