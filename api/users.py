# -*- coding: utf-8 -*-

"""
    User related api
"""

from flask import Blueprint
from services import UserService
from services import RegisterService, LoginService, LogoutService, SNSLoginService
from models import *
from pbmodels.user_pb2 import *
from flask import session, request
from common.utils.upload_util import *

bp = Blueprint('users', __name__, url_prefix='/api/users')

@bp.route('/register')
def register():
    return RegisterService(request).handle()

@bp.route('/login')
def login():
    return LoginService(request).handle()

@bp.route('/logout')
def logout():
    return LogoutService(request).handle()

@bp.route('/snslogin')
def snslogin():
    return SNSLoginService(request).handle()

@bp.route('/upload', methods=['GET','POST'])
def upload():
    if request.method == 'POST':
        file = request.files['file']
        return upload_file(file, 'upload')
    
    return  """
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form action="" method=post enctype=multipart/form-data>
      <p><input type=file name=file>
           <input type=submit value=Upload>
     </form>
     """

#Below is test code 

@bp.route('/add')
def add_user():
    pb_user = PBUser()
    pb_user.basic_info.uname = 'kk'
    pb_user.basic_info.nick = 'kk'
    print pb_user

    user = User()
    basic_info = UserBasic()
    basic_info.uname = pb_user.basic_info.uname
    basic_info.nick = pb_user.basic_info.nick

    user.basic_info = basic_info
    userService = UserService()
    userService.save(user)

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

@bp.route("/set")
def set_session():
    session['uid'] = request.args.get('uid')
    session['name'] = request.args.get('name')
    return session['uid']

@bp.route("/get")
def get_session():
    if 'uid' in session:
        print session.get('uid')
    return session.get('uid', '')

@bp.route("/remove")
def remove_session():
    if 'uid' in session:
        session.pop('uid',None)
    return ''

@bp.route("/delete")
def delete_session():
    if 'uid' in session:
        session.clear()
    return ''
