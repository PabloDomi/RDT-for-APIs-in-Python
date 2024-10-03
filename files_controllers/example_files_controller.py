import click
import time
from colorama import Fore
from implementations.Flask_Restx.TortoiseORM.files_flask_tortoiseORM import code_models_flask_tortoiseORM, code_route_flask_tortoiseORM, code_jwt_route_flask_tortoiseORM
from implementations.Flask_Restx.SQLAlchemy.files_flask_sqlalchemy import code_models_flask_sqlalchemy, code_route_flask_sqlalchemy, code_jwt_route_flask_sqlalchemy
from implementations.Flask_Restx.Pewee.files_flask_pewee import code_route_flask_pewee, code_models_flask_pewee, code_jwt_route_flask_pewee


def create_example_files(auth, framework, orm):
    # Crear ejemplos en models y routes

    # =================== FLASK =================== #

    if framework == 'Flask-Restx':

        # ======= SQLAlchemy ======= #
        if orm == 'SQLAlchemy':
            try:
                with open('src/routes/routes_example.py', 'w') as f:
                    if auth == 'No':
                        f.write(code_route_flask_sqlalchemy())
                    elif auth == 'Sí':
                        f.write(code_jwt_route_flask_sqlalchemy())
            except Exception as e:
                print("No se ha podido escribir en el archivo routes_example: ", e)

            with open('src/models/models.py', 'w') as f:
                f.write(code_models_flask_sqlalchemy())

        # ======= TortoiseORM ======= #
        elif orm == 'TortoiseORM':
            with open('src/routes/routes_example.py', 'w') as f:
                if auth == 'No':
                    f.write(code_route_flask_tortoiseORM())
                elif auth == 'Sí':
                    f.write(code_jwt_route_flask_tortoiseORM())

            with open('src/models/models.py', 'w') as f:
                f.write(code_models_flask_tortoiseORM())

        # ======= Pewee ======= #
        if orm == 'Pewee':
            with open('src/routes/routes_example.py', 'w') as f:
                if auth == 'No':
                    f.write(code_route_flask_pewee())
                elif auth == 'Sí':
                    f.write(code_jwt_route_flask_pewee())

            with open('src/models/models.py', 'w') as f:
                f.write(code_models_flask_pewee())

    # =================== FASTAPI =================== #

    elif framework == 'FastAPI':
        with open('src/routes/routes_example.py', 'w') as f:
            f.write('''from fastapi import APIRouter

                router = APIRouter()

                @router.get("/hello")
                def hello_world():
                    return {"message": "Hello, World!"}
            ''')

    click.echo(Fore.YELLOW + 'Ejemplos generados en models y routes.')
    time.sleep(0.5)
