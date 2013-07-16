# -*- coding: utf-8 -*-

"""
    User related api
"""

from flask import Blueprint
from services import UserService
from models import UserBasic, User
from pbmodels.user_pb2 import *
from services import RegisterService
from flask import request

bp = Blueprint('users', __name__, url_prefix='/api/users')

@bp.route('/add', methods=['GET'])
def add_user():
    return RegisterService(request).handle()

@bp.route('/list')
def list_user():
    userService = UserService()
    users = userService.find()
    return ""

@bp.route('/count')
def count_user():
    userService = UserService()
    users = userService.find()
    count = users.count()
    return str(count)

@bp.route('/update')
def update_user():
    return ''
pass
