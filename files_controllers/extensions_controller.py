import click
import time
from colorama import Fore
from implementations.Flask_Restx.SQLAlchemy.extensions_flask_sqlalchemy import code_extensions_flask_sqlalchemy, code_extensions_jwt_flask_sqlalchemy
from implementations.Flask_Restx.TortoiseORM.extensions_flask_tortoise import code_extensions_flask_tortoiseORM
from implementations.Flask_Restx.Pewee.extensions_flask_pewee import code_extensions_flask_pewee, code_jwt_extensions_flask_pewee


def create_extensions_file(framework, orm, auth, db):
    with open('src/extensions.py', 'w') as f:
        f.write('\n\n')

        # =================== FLASK-RESTX =================== #

        if framework == 'Flask-Restx':

            # ======= SQLAlchemy ======= #
            if orm == 'SQLAlchemy':
                f.write(code_extensions_flask_sqlalchemy())

                if auth == 'Sí':
                    f.write(code_extensions_jwt_flask_sqlalchemy())

            # ======= TortoiseORM ======= #
            elif orm == 'TortoiseORM':
                f.write(code_extensions_flask_tortoiseORM())

            # ======= Pewee ======= #
            elif orm == 'Pewee':
                f.write(code_extensions_flask_pewee())

                if auth == 'Sí':
                    f.write(code_jwt_extensions_flask_pewee())

        # =================== FASTAPI =================== #

        elif framework == 'FastAPI':
            f.write('from fastapi import FastAPI\n\napp = FastAPI()\n\n')
            if orm == 'SQLAlchemy':
                f.write('from sqlalchemy import create_engine\nfrom sqlalchemy.engine import URL\nfrom sqlalchemy.orm import sessionmaker\n\n')

                if db == 'PostgreSQL':
                    f.write('url = URL.create(drivername="postgresql", username="postgres", password="", host="localhost", database="example", port=5432)\n\n')
                elif db == 'MySQL':
                    f.write('url = URL.create(drivername="mysql", username="root", password="", host="localhost", database="example", port=3306)\n\n')
                elif db == 'SQLite':
                    f.write('url = URL.create(drivername="sqlite", database="example.db")\n\n')

                f.write('engine = create_engine(url)\nSession = sessionmaker(autocommit=False, autoflush=False, bind=engine)\nsession=Session()\n\n')

            if auth == 'Sí':
                f.write('from fastapi.security import OAuth2PasswordBearer\nfrom passlib.context import CryptContext\n\n')
                f.write('pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")\noauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")\n')

    click.echo(Fore.YELLOW + 'Archivo extensions.py generado.')
    time.sleep(0.5)
