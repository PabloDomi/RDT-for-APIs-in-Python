

def code_extensions_flask_sqlalchemy():
    code = '''
from flask_restx import Api
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

api = Api()
migration = Migrate()
login_manager = LoginManager()
db = SQLAlchemy()


    '''
    return code


def code_extensions_jwt_flask_sqlalchemy():
    code = '''
from flask_jwt_extended import JWTManager

jwt = JWTManager()
    '''
    return code
