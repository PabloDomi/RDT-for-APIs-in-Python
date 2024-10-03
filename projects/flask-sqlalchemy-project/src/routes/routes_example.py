
from src.models.models import User
from flask_restx import Resource, Namespace
from src.extensions import db

user_ns = Namespace('users', description='User operations')


@user_ns.route('/')
class UserList(Resource):
    def get(self):
        users = User.query.all()
        return [{"id": user.id, "username": user.username} for user in users]

    def post(self):
        # Ejemplo para crear un usuario
        new_user = User(username='example', password='password')
        db.session.add(new_user)
        db.session.commit()
        return {"id": new_user.id, "username": new_user.username}, 201
