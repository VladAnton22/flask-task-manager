from .task_routes import task_bp
from .auth_routes import auth_bp

def register_routes(app):
    app.register_blueprint(task_bp)
    app.register_blueprint(auth_bp)