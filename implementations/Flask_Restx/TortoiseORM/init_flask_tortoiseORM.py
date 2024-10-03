

def code_init_flask_tortoiseORM():
    code = '''
from flask import Flask
from src.config.config import Config
from src.extensions import init_tortoise, api
from src.routes.routes_example import user_ns
from dotenv import load_dotenv


def create_app():
    load_dotenv()

    app = Flask(__name__)
    app.config.from_object(Config)

    # Inicializar Flask Restx
    api.init_app(app)

    # Inicializar Tortoise ORM
    init_tortoise(app)

    # Registrar rutas y blueprints
    api.add_namespace(user_ns)

    return app
    '''

    return code
