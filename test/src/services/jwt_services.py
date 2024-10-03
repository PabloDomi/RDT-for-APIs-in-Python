from functools import wraps
from flask import request, jsonify
from src.models.models import User
import jwt
from dotenv import load_dotenv
import os


load_dotenv()

SECRET_KEY = os.getenv('SECRET_KEY')


# Decorator para verificar si el usuario esta autenticado
def jwt_required(f):
    @wraps(f)
    async def decorated(*args, **kwargs):
        token = None
        # Verificar si el token está en la cabecera 'Authorization'
        if 'Authorization' in request.headers:
            token = request.headers['Authorization'].split()[1]  # Bearer <token>

        if not token:
            return jsonify({'message': 'Token is missing!'}), 401

        try:
            # Decodificar el token
            data = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
            current_user = await User.get(id=data['user_id'])  # Cargar el usuario con Tortoise-ORM
        except jwt.ExpiredSignatureError:
            return jsonify({'message': 'Token has expired!'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'message': 'Invalid token!'}), 401
        except User.DoesNotExist:
            return jsonify({'message': 'User not found!'}), 404

        # Llamar a la función decorada y pasar el usuario actual como parámetro
        return await f(current_user, *args, **kwargs)

    return decorated


# Función para obtener la identidad del usuario del token JWT
def get_jwt_identity():
    token = None
    if 'Authorization' in request.headers:
        token = request.headers['Authorization'].split()[1]  # Bearer <token>

    if token:
        try:
            data = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
            return data['user_id']  # Extraer el user_id del payload
        except jwt.ExpiredSignatureError:
            return None  # El token ha expirado
        except jwt.InvalidTokenError:
            return None  # El token es inválido
    return None
