from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from website.SERVICE.Service import get_config


db = SQLAlchemy()

config = get_config()


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'Test'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{config["DataBase_Info"]["DB_NAME"]}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    creat_database(app)
    return app


def creat_database(app):
    if not path.exists('website/' + config["DataBase_Info"]["DB_NAME"]):
        db.create_all(app=app)
        print('Created Database !')
