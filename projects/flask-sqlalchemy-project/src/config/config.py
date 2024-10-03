
import os


class Config:

    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'default_secret')
    FLASK_RUN_PORT = os.environ.get('FLASK_RUN_PORT')
    FLASK_APP = os.environ.get('FLASK_APP')
    FLASK_ENV = 'development'
    FLASK_DEBUG = 'DEBUG'
        
    SQLALCHEMY_TRACK_MODIFICATIONS = False
            
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI_DEV')
            

# class ProductionConfig(Config):
#     JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'default_secret')
#     FLASK_RUN_PORT = os.environ.get('FLASK_RUN_PORT')
#     FLASK_APP = os.environ.get('FLASK_APP')
#     FLASK_ENV = 'production'
#     FLASK_DEBUG = False
        
    # SQLALCHEMY_TRACK_MODIFICATIONS = False
            
    # SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI_DEV')
            
    # SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI_PROD')
            