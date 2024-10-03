import click
import time
from colorama import Fore


def create_requirements_txt(framework, orm, auth, db):
    requirements = []

    requirements.append('python-dotenv\npathlib\n\n# Automated tests\npytest\npytest-cov\n')

    if framework != 'Flask':
        if db == 'PostgreSQL':
            requirements.append('asyncpg\n')
        elif db == 'MySQL':
            requirements.append('aiomysql\n')
        elif db == 'SQLite':
            requirements.append('aiosqlite\n')
    else:
        if db == 'PostgreSQL':
            requirements.append('psycopg2-binary\n')
        elif db == 'MySQL':
            requirements.append('mysqlclient\n')
        elif db == 'SQLite':
            requirements.append('sqlite3\n')

    if framework == 'FastAPI':
        requirements.append('fastapi\nuvicorn\n')
        if auth == 'Sí':
            requirements.append('fastapi-jwt-auth\npasslib[bcrypt]\n')
    elif framework == 'Flask-Restx':
        requirements.append('Flask\nFlask-restx\nFlask-Login\n')
        if auth == 'Sí':
            requirements.append('flask-jwt-extended\npasslib[bcrypt]\n')
    elif framework == 'Django-Rest':
        requirements.append('djangorestframework\nmarkdown\ndjango-filter\ndjango-silk\n')
    elif framework == 'Tornado':
        requirements.append('tornado\naio\nmustache\n')
    elif framework == 'Sanic':
        requirements.append('sanic\ninjector\nopenapi-generator\n')
    elif framework == 'Falcon':
        requirements.append('falcon\n[gunicorn|uwsgi|waitress]\n[uvicorn|daphne|hypercorn]\n')
    elif framework == 'Hug':
        requirements.append('hug\nfalcon\nbandit\nsafety\n')

    if orm == 'SQLAlchemy':
        requirements.append('sqlalchemy\npsycopg2-binary\n')

        if framework in ['Flask-Restx']:
            # Quitar "sqlalchemy" de requirements (NO FUNCIONA)
            # requirements.remove('sqlalchemy\n')
            requirements.append('flask-sqlalchemy\nFlask-Migrate\n')

        elif framework == 'FastAPI':
            requirements.append('alembic\n')

        elif framework == 'Tornado':
            requirements.append('tornado_sqlalchemy\nsqlalchemy\n')

    elif orm == 'TortoiseORM':
        requirements.append('tortoise-orm\naerich\n')
        if auth == 'Sí' and framework == 'Flask-Restx':
            requirements.append('pyjwt\nfunctools\n')

    elif orm == 'DjangoORM':
        requirements.append('Django\n')

    elif orm == 'Pewee':
        requirements.append('pewee\npewee-migrate\n')
        if auth == 'Sí' and framework == 'Flask-Restx':
            requirements.append('flask-pewee\n')
        if auth == 'Sí' and framework == 'FastAPI':
            requirements.append('pewee-async\n')

    with open('requirements.txt', 'w') as f:
        f.writelines(requirements)

    click.echo(Fore.YELLOW + 'Archivo requirements.txt generado.')
    time.sleep(0.5)
