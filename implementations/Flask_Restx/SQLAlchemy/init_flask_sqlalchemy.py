

def code_init_flask_sqlalchemy():
    code = '''
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
    '''

    return code


def code_init_jwt_flask_sqlalchemy():
    code = '''
from dotenv import load_dotenv
from flask import Flask
from src.config.config import Config
from .extensions import api, db, jwt, migration
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

    # Initialize the app with the jwt
    jwt.init_app(app)

    # Initialize the app with the migration
    migration.init_app(app, db)

    api.add_namespace(user_ns)

    return app


# Se guarda en el campo "sub" del token el id del usuario
@jwt.user_identity_loader
def user_identity_lookup(user):
    return user.id


# Se busca el usuario por el id guardado en el campo "sub" del token
@jwt.user_lookup_loader
def user_lookup_callback(_jwt_header, jwt_data):
    identity = jwt_data["sub"]
    return User.query.filter_by(id=identity).one_or_none()
    '''

    return code
