import os

from flask import Flask

from apps import register_blueprints, errors
from extensions import extension_init


class Config():
    database_uri = 'sqlite:///' + os.path.join(os.getcwd(), 'mydb.sqlite3')
    SQLALCHEMY_DATABASE_URI = database_uri
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = '123'
    MAIL_USERNAME = '396624059@qq.com'
    MAIL_PASSWORD = 'crcdetixcfejbgea'
    MAIL_SERVER = 'smtp.qq.com'
    MAIL_USE_TLS = True

    MAX_CONTENT_LENGTH = 8 * 1024 * 1024
    UPLOADED_PHOTOS_DEST = os.path.join(os.getcwd(),'static/uploads')


def db_config(app):
    '''从类中获取config'''
    app.config.from_object(Config)


def create_app():
    global app
    app = Flask(__name__)
    register_blueprints(app)
    errors(app)
    # base_dir = os.path.abspath(os.path.dirname(__file__))
    db_config(app)
    extension_init(app)
    return app