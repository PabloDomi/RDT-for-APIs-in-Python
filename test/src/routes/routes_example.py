
from flask_restx import Resource, Namespace
from src.models.models import User
import jwt
from flask_restx import fields
from src.services.jwt_services import jwt_required, SECRET_KEY, get_jwt_identity

authorizations = {
    "jsonWebToken": {
        "type": "apiKey",
        "in": "header",
        "name": "Authorization"
    }
}

user_ns = Namespace("auth", description="Auth operations", authorizations=authorizations)


@user_ns.route('/register')
class Register(Resource):

    @user_ns.expect(user_ns.model("User", {
        "username": fields.String(required=True),
        "password": fields.String(required=True)
    }))
    async def post(self):
        data = user_ns.payload
        username = data.get("username")
        password = data.get("password")

        user = await User.create(username=username, password=password)

        user_with_id = await User.get(username=username)

        access_token = jwt.encode({
            "user_id": user_with_id.username
            }, SECRET_KEY, algorithm='HS256'
        )

        user_with_id.access_token = access_token

        return {"id": user.id, "username": user.username, "access_token": access_token}, 201


@user_ns.route('/protectedUserRoute')
class ProtectedUserRoute(Resource):
    @user_ns.expect(user_ns.model("User", {
        "username": fields.String(required=True),
        "password": fields.String(required=True)
    }))
    @user_ns.doc(security='jsonWebToken')
    @jwt_required
    async def post(self):
        current_user = get_jwt_identity()

        user = await User.get(current_user)
        if user:
            return {"id": user.id, "username": user.username, "access_token": user.access_token}
        else:
            return {"message": "User not found"}, 404
