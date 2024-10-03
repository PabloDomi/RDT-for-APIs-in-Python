

def code_extensions_flask_tortoiseORM():
    code = '''
from flask_restx import Api
from tortoise.contrib.flask import register_tortoise

api = Api()


def init_tortoise(app):
    register_tortoise(
        app,
        db_url=app.config['SQLALCHEMY_DATABASE_URI_DEV'],
        modules={"models": app.config['TORTOISE_ORM']['apps']['models']['models']},
        generate_schemas=False,  # Las migraciones se manejan con Aerich
        add_exception_handlers=True,
    )

    '''

    return code
