
from dotenv import load_dotenv
from flask import Flask
from src.config.config import Config
from .extensions import api, db, migration
from src.models.models import User
from src.routes.routes_example import user_ns


def create_app():

    load_dotenv()

    app = Flask(__name__)

    app.config.from_object(Config)

    # Instance of db
    db.init_app(app)

    # Initialize the app with the api
    api.init_app(app)

    # Initialize the app with the migration
    migration.init_app(app, db)

    api.add_namespace(user_ns)

    return app
    