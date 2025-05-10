from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__, template_folder='templates', static_folder='static')

    # config setup
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///task_manage.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'secret-key'

    # initialize extensions
    db.init_app(app)
    from .models import User
    migrate.init_app(app, db)

    # register routes
    from .routes import register_routes
    register_routes(app)

    return app
