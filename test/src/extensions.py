from tortoise import Tortoise
from flask_restx import Api
import asyncio
import os
from dotenv import load_dotenv

load_dotenv()

api = Api()


def init_tortoise(app):
    loop = asyncio.get_event_loop()
    loop.run_until_complete(Tortoise.init(
            app,
            db_url=os.getenv('SQLALCHEMY_DATABASE_URI_DEV'),
            modules={"models": ["src.models.models"]}
        )
    )
