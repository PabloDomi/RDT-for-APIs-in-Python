

def code_jwt_init_flask_pewee():
    code = '''
from flask import Flask
from src.Config.config import Config
from src.extensions import db, jwt, api, migration
from src.models.models import User
from src.routes import user_ns
from dotenv import load_dotenv


def create_app():

    load_dotenv()

    app = Flask(__name__)
    app.config.from_object(Config)

    # Inicializar Peewee (Flask-Peewee)
    db.init_app(app)

    # Inicializar JWT
    jwt.init_app(app)

    # Inicializar Flask-Restx
    api.init_app(app)

    # Inicializar Flask-Migrate
    migration.init_app(app, db)

    # Registrar rutas y blueprints
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


def code_init_flask_pewee():
    code = '''
from flask import Flask
from src.Config.config import Config
from src.extensions import db, api, migration
from src.models.models import User
from src.routes import user_ns
from dotenv import load_dotenv


def create_app():

    load_dotenv()

    app = Flask(__name__)
    app.config.from_object(Config)

    # Inicializar Peewee (Flask-Peewee)
    db.init_app(app)

    # Inicializar Flask-Restx
    api.init_app(app)

    # Inicializar Flask-Migrate
    migration.init_app(app, db)

    # Registrar rutas y blueprints
    api.add_namespace(user_ns)

    return app
    '''

    return code
