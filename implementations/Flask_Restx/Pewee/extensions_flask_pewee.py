

def code_extensions_flask_pewee():
    code = '''

from flask_peewee.db import Database
from flask_restx import Api
from flask_migrate import Migrate


migration = Migrate()
api = Api()
db = Database()
    '''

    return code


def code_jwt_extensions_flask_pewee():
    code = '''

from flask_jwt_extended import JWTManager

jwt = JWTManager()
    '''

    return code
