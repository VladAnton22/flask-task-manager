from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, DateField, SelectField
from wtforms.validators import InputRequired, EqualTo, Optional

class AddATask(FlaskForm):
    title = StringField("Title:", validators=[InputRequired()])
    description = StringField("Descriptiton:", validators=[Optional()])
    due_date = DateField("Due Date:", validators=[Optional()])
    priority = SelectField(
        "Priority",
        choices=[
            ("1", "Very Low"),
            ("2", "Low"),
            ("3", "Medium"),
            ("4", "High"),
            ("5", "Urgent")
        ],
        default="3"
    )
    status = SelectField(
        "Status",
        choices=[
            ("todo", "To Do"),
            ("in_progress", "In Progress"),
            ("done", "Done")
        ],
        default="todo"
    )
    submit = SubmitField("Create Task")

class RegistrationForm(FlaskForm):
    name = StringField("Username", validators=[InputRequired()])
    password = PasswordField("Password", validators=[InputRequired()])
    password2 = PasswordField("Repeat Password", validators=[InputRequired(), EqualTo("password")])
    submit = SubmitField("Register")

class LoginForm(FlaskForm):
    name = StringField("Username", validators=[InputRequired()])
    password = PasswordField("Password", validators=[InputRequired()])
    submit = SubmitField("Log in")
