from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__, template_folder='templates', static_folder='static')

    # config setup
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///task_manage.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'secret-key'

    # initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    from .models import User
    from .routes import register_routes
    register_routes(app)

    return app

from .models import User

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int((user_id)))
