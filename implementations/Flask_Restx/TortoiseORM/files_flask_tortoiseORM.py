

def code_models_flask_tortoiseORM():
    code = '''
from tortoise import fields, models


class User(models.Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=255, unique=True)
    password = fields.CharField(max_length=255)
    access_token = fields.CharField(max_length=400)

    def __str__(self):
        return self.username
    '''

    return code


def code_route_flask_tortoiseORM():
    code = '''
from flask_restx import Resource, Namespace
from src.models import User

user_ns = Namespace("users", description="User operations")

@user_ns.route('/')
class UserList(Resource):
    async def get(self):
        users = await User.all()
        return [{"id": user.id, "username": user.username} for user in users]

    async def post(self):
        # Ejemplo para crear un usuario
        new_user = await User.create(username="example", password="password")
        return {"id": new_user.id, "username": new_user.username}, 201

    '''

    return code


def code_jwt_route_flask_tortoiseORM():
    code = '''
from flask_restx import Resource, Namespace
from src.models import User
import jwt

user_ns = Namespace("auth", description="Auth operations")

@user_ns.route('/login')
class Login(Resource):
    async def post(self):
        # Ejemplo de autenticación
        data = user_ns.payload
        username = data.get("username")
        password = data.get("password")

        user = await User.get(username=username)
        if user and user.password == password:
            access_token = jwt.encode(identity=user.username)
            return {"access_token": access_token}, 200
        return {"message": "Invalid credentials"}, 401

    '''

    return code
