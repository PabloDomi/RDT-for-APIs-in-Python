

def code_models_flask_sqlalchemy():
    code = '''
from src.extensions import db

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    access_token = db.Column(db.String(400))
    '''

    return code


def code_route_flask_sqlalchemy():
    code = '''
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

    '''
    return code


def code_jwt_route_flask_sqlalchemy():
    code = '''
from src.models.models import User
from flask_restx import Resource, Namespace
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from src.extensions import db, api
from flask_restx import fields

authorizations = {
    "jsonWebToken": {
        "type": "apiKey",
        "in": "header",
        "name": "Authorization"
    }
}

user_ns = Namespace('auth', description='Auth operations', authorizations=authorizations)


@user_ns.route('/register')
class Register(Resource):
    # Este modelo debería ir ubicado en un archivo api_models.py dentro de la carpeta models y luego importarlo
    @user_ns.expect(api.model('User', {
        "username": fields.String,
        "password": fields.String
    }))
    def post(self):
        data = user_ns.payload
        username = data.get("username")
        password = data.get("password")

        user = User(
            username=username,
            password=password,
            access_token=None
        )

        db.session.add(user)

        user_with_id = User.query.filter_by(username=username).first()

        access_token = create_access_token(user_with_id)

        user.access_token = access_token

        db.session.commit()
        return {"message": "Register"}, 200


@user_ns.route('/protectedUserRoute')
class ProtectedUserRoute(Resource):
    method_decorators = [jwt_required()]

    @user_ns.doc(security='jsonWebToken')
    def get(self):
        current_user_id = get_jwt_identity()
        user = User.query.get(current_user_id)
        if user:
            return {"id": user.id, "username": user.username, "access_token": user.access_token}
        else:
            return {"message": "User not found"}, 404

    '''
    return code
