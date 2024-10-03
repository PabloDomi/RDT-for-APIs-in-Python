import time
import click
from colorama import Fore


def create_config_file(framework, orm, db):

    if db == 'PostgreSQL':
        engine = 'postgresql'
        pewee_engine = 'PostgresqlDatabase'
    elif db == 'MySQL':
        engine = 'mysql'
        pewee_engine = 'MySQLDatabase'
    elif db == 'SQLite':
        engine = 'sqlite3'
        pewee_engine = 'SqliteDatabase'

    with open('src/config/config.py', 'w') as f:
        f.write('''
import os


class Config:

    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'default_secret')
    FLASK_RUN_PORT = os.environ.get('FLASK_RUN_PORT')
    FLASK_APP = os.environ.get('FLASK_APP')
    FLASK_ENV = 'development'
    FLASK_DEBUG = 'DEBUG'
        ''')

        if framework == 'Flask-Restx' and orm == 'TortoiseORM':
            f.write(f'''
    TORTOISE_ORM = {{
        "connections": {{
            "default": os.getenv("DATABASE_URL", "sqlite://db.{engine}"),
        }},
        "apps": {{
            "models": {{
                "models": ["src.models", "aerich.models"],
                "default_connection": "default",
            }},
        }},
    }}

    TORTOIRSE_ORM_URI = os.getenv('SQLALCHEMY_DATABASE_URI_DEV')
            ''')
        elif framework == 'Flask-Restx' and orm == 'SQLAlchemy':
            f.write('''
    SQLALCHEMY_TRACK_MODIFICATIONS = False
            ''')

        elif framework == 'Flask-Restx' and orm == 'Pewee':
            f.write(f'''
    DATABASE = {{
        'name': os.getenv('DATABASE_URL', 'peewee_app.db'),
        'engine': 'peewee.{pewee_engine}'
    }}
            ''')

        if orm == 'SQLAlchemy':
            f.write('''
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI_DEV')
            ''')

        f.write('''\n
# class ProductionConfig(Config):
#     JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'default_secret')
#     FLASK_RUN_PORT = os.environ.get('FLASK_RUN_PORT')
#     FLASK_APP = os.environ.get('FLASK_APP')
#     FLASK_ENV = 'production'
#     FLASK_DEBUG = False
        ''')
        if framework == 'Flask-Restx' and orm == 'tortoiseORM':
            f.write(f'''
    # TORTOISE_ORM = {{
    #     "connections": {{
    #         "default": os.getenv("DATABASE_URL", "sqlite://db.{engine}"),
    #     }},
    #     "apps": {{
    #         "models": {{
    #             "models": ["src.models", "aerich.models"],
    #             "default_connection": "default",
    #         }},
    #     }},
    # }}
            ''')
        elif framework == 'Flask-Restx' and orm == 'SQLAlchemy':
            f.write('''
    # SQLALCHEMY_TRACK_MODIFICATIONS = False
            ''')

        elif framework == 'Flask-Restx' and orm == 'Pewee':
            f.write(f'''
    # DATABASE = {{
    #     'name': os.getenv('DATABASE_URL', 'peewee_app.db'),
    #     'engine': 'peewee.{pewee_engine}'
    # }}
            ''')

        if orm == 'SQLAlchemy':
            f.write('''
    # SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI_DEV')
            ''')

        if orm == 'SQLAlchemy':
            f.write('''
    # SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI_PROD')
            ''')

    click.echo(Fore.YELLOW + 'Archivo config.py generado.')
    time.sleep(0.5)
