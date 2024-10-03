

def code_models_flask_pewee():
    code = '''
from peewee import CharField
from src.extensions import db
from passlib.hash import bcrypt

class User(db.Model):
    username = CharField(unique=True)
    password_hash = CharField()

    def verify_password(self, password):
        return bcrypt.verify(password, self.password_hash)

    @classmethod
    def create_user(cls, username, password):
        password_hash = bcrypt.hash(password)
        return cls.create(username=username, password_hash=password_hash)
    '''

    return code


def code_route_flask_pewee():
    code = '''
from flask_restx import Resource, Namespace
from src.models.models import User

user_ns = Namespace("users", description="User operations")

@user_ns.route('/')
class UserList(Resource):
    def get(self):
        users = User.select()
        return [{"id": user.id, "username": user.username} for user in users]
    '''

    return code


def code_jwt_route_flask_pewee():
    code = '''

from flask_restx import Resource, Namespace
from src.models.models import User
from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token

authorizations = {
    "jsonWebToken": {
        "type": "apiKey",
        "in": "header",
        "name": "Authorization"
    }
}

user_ns = Namespace("auth", description="Auth operations", authorizations=authorizations)

@user_ns.route('/protectedUserRoute')
class ProtectedUserRoute(Resource):
    method_decorators = [jwt_required()]
    user_ns.doc(security='jsonWebToken')

    def get(self):
        current_user_id = get_jwt_identity()
        user = User.query.get(current_user_id)
        if user:
            return {"id": user.id, "username": user.username, "access_token": create_access_token(identity=user.id)}
        else:
            return {"message": "User not found"}, 404

    '''

    return code
