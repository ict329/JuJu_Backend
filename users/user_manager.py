# -*- coding: utf-8 -*-
# -*- 2013-07-16 -*-

from users.user import *

def get_user(uid):
    try:
        return User.objects.get(pk=uid)
    except:
        return None

def get_user_by_uname(uname):
    try:
        return User.objects.get(basic_info__uname = uname)
    except:
        return None

def register(uname, password):
    user = User()
    basic = UserBasic()
    basic.uname = uname
    basic.password = password
    basic.nick = uname
    user.basic_info = basic
    try:
        user.save()
        return user
    except:
        return None



    def __init__(self, uname, password):
        basic = UserBasic(uname = uname, password = password, nick = uname)
        self.basic_info = basic
        self.save()
    def __init__(self, uname, password):
        basic = UserBasic(uname = uname, password = password, nick = uname)
        self.basic_info = basic
        self.save()
    def __init__(self, uname, password):
        basic = UserBasic(uname = uname, password = password, nick = uname)
        self.basic_info = basic
        self.save()
