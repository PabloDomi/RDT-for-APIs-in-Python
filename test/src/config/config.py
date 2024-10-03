
import os


class Config:

    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'default_secret')
    FLASK_RUN_PORT = os.environ.get('FLASK_RUN_PORT')
    FLASK_APP = os.environ.get('FLASK_APP')
    FLASK_ENV = 'development'
    FLASK_DEBUG = 'DEBUG'
    TORTOIRSE_ORM_URI = os.getenv('SQLALCHEMY_DATABASE_URI_DEV')

    TORTOISE_ORM = {
        "connections": {
            "default": os.getenv("DATABASE_URL", "sqlite://db.sqlite3"),
        },
        "apps": {
            "models": {
                "models": ["src.models", "aerich.models"],
                "default_connection": "default",
            },
        },
    }

# class ProductionConfig(Config):
#     JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'default_secret')
#     FLASK_RUN_PORT = os.environ.get('FLASK_RUN_PORT')
#     FLASK_APP = os.environ.get('FLASK_APP')
#     FLASK_ENV = 'production'
#     FLASK_DEBUG = False
