# -*- coding: utf-8 -*-

"""
    User related api
"""

from flask import Blueprint
from services import UserService
from models import UserBasic, User
from pbmodels.user_pb2 import *

bp = Blueprint('users', __name__, url_prefix='/api/users')

@bp.route('/add')
def add_user():
    pb_user = PBUser()
    pb_user.basic_info.uname = 'kaibin'
    pb_user.basic_info.uid = '1'
    pb_user.basic_info.nick = 'kaibin'
    print pb_user

    user = User()
    basic_info = UserBasic()
    basic_info.uid = pb_user.basic_info.uid
    basic_info.uname = pb_user.basic_info.uname
    basic_info.nick = pb_user.basic_info.nick

    user.basic_info = basic_info
    userService = UserService()
    userService.save(user)
    return ''

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