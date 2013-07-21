# -*- coding: utf-8 -*-

from flask import *
from helpers import register_blueprints
import api
from mongoengine import connect
from settings import * 
#from core.session import RedisSessionInterface

def create_app():
    app = Flask(__name__)
    app.config.from_object("settings")
#    app.session_interface = RedisSessionInterface()
    return app

def register_all_blueprints(app):
    """
        注册app应用api包路径下的所有蓝图
    """
    register_blueprints(app, api.__name__, api.__path__)

@app.route("/favicon.ico")
def favicon():
    return ''

app = create_app()
register_all_blueprints(app)
connect(DATABASE, host = MONGO_HOST, port = MONGO_PORT)

#App Settings
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if __name__ == '__main__':
    app.run()
