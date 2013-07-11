# -*- coding: utf-8 -*-

from flask import *
from helpers import register_blueprints
import api
from mongoengine import connect
from settings import MONGO_CONFIG

def create_app():
    app = Flask(__name__)
    app.config.from_object("settings")
    return app

def register_all_blueprints(app):
    """
        注册app应用api包路径下的所有蓝图
    """
    register_blueprints(app, api.__name__, api.__path__)

app = create_app()
register_all_blueprints(app)
connect(MONGO_CONFIG['DB'], host = MONGO_CONFIG['HOST'], port = MONGO_CONFIG['PORT'])

if __name__ == '__main__':
    app.run()