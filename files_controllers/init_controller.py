import click
import time
from colorama import Fore
from implementations.Flask_Restx.TortoiseORM.init_flask_tortoiseORM import code_init_flask_tortoiseORM
from implementations.Flask_Restx.SQLAlchemy.init_flask_sqlalchemy import code_init_flask_sqlalchemy, code_init_jwt_flask_sqlalchemy
from implementations.Flask_Restx.Pewee.init_flask_pewee import code_init_flask_pewee, code_jwt_init_flask_pewee


def create_init_file(auth, framework, db, orm):
    # =================== FLASK-RESTX =================== #

    if framework == 'Flask-Restx':
        try:
            with open('src/__init__.py', 'w') as f:

                # ======= SQLAlchemy ======= #
                if orm == 'SQLAlchemy' and auth == 'Sí':
                    f.write(code_init_jwt_flask_sqlalchemy())
                elif orm == 'SQLAlchemy' and auth == 'No':
                    f.write(code_init_flask_sqlalchemy())

                # ======= TortoiseORM ======= #
                elif orm == 'TortoiseORM':
                    f.write(code_init_flask_tortoiseORM())

                # ======= Pewee ======= #
                elif orm == 'Pewee' and auth == 'Sí':
                    f.write(code_jwt_init_flask_pewee())
                elif orm == 'Pewee' and auth == 'No':
                    f.write(code_init_flask_pewee())
        except Exception as e:
            print("No se ha podido escribir en el archivo __init__: ", e)

    # =================== FASTAPI =================== #

    elif framework == 'FastAPI':
        with open('src/__init__.py', 'w') as f:

            # ======= SQLAlchemy ======= #
            if orm == 'SQLAlchemy':
                f.write()

            # ======= TortoiseORM ======= #
            if orm == 'TortoiseORM':
                f.write()

            # ======= Pewee ======= #
            if orm == 'Pewee':
                f.write()

    click.echo(Fore.YELLOW + 'Archivo __init__.py generado.')
    time.sleep(0.5)
