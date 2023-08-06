from pathlib import Path

from flask import Flask
from flask_wtf.csrf import CSRFProtect

BASE_DIR = Path(__file__).parent

class Config:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + str(BASE_DIR.joinpath('db.sqlite'))
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'teste'


def create_app(config_obj=Config):
    app = Flask(__name__)
    app.config.from_object(config_obj)

    from models import db
    db.init_app(app)

    csrf = CSRFProtect(app)
    csrf.init_app(app)

    return app
