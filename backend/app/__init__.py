from flask import Flask
from .database import db
from .routes import main
from flask_migrate import Migrate
from flasgger import Swagger
from flask_cors import CORS

def create_app():
    """Create and configure the Flask application."""
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///titanic.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    Migrate(app, db)

    app.register_blueprint(main)

    swagger = Swagger(app)
    CORS(app)  # Enable CORS for all routes

    return app