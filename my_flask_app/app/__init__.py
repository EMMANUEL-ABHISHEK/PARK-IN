# app/__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
import os

# Initialize extensions
db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
bcrypt = Bcrypt()

# Setting up the login view
login_manager.login_view = 'main_bp.login'
login_manager.login_message_category = 'info'

def create_app(config_class=None):
    app = Flask(__name__, instance_relative_config=True)

    # Load the configuration from config.py or environment variables
    if config_class:
        app.config.from_object(config_class)
    else:
        app.config.from_pyfile('config.py', silent=True)

    # Fallback to default configuration if needed
    app.config.setdefault('SQLALCHEMY_DATABASE_URI', os.getenv('DATABASE_URL', 'sqlite:///site.db'))
    app.config.setdefault('SECRET_KEY', os.getenv('SECRET_KEY', '240b297103199d8c322f0e5dd215188ddcf3153f3ffe3304b667392ce40b1518'))
    app.config.setdefault('SQLALCHEMY_TRACK_MODIFICATIONS', False)

    # Initialize extensions with the app
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    bcrypt.init_app(app)

    # Import and register blueprints
    from .routes import main_bp
    app.register_blueprint(main_bp)

    return app
