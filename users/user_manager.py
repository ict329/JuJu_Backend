#-*- coding: utf-8 -*-
# -*- 2013-07-16 -*-

from users.user import *
import datetime
import pbmodels.user_pb2 as user_pb2
import constant.para as para


def login(uname, password):
    return User.objects.get(basic_info__uname = uname, basic_info__password = password)

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

def register(uname, password, **fields):
    user = User()
    
    basic = UserBasic()
    basic.uname = uname
    basic.password = password
    basic.nick = uname
    user.basic_info = basic

    reg_info = Registration()
    reg_info.reg_date = datetime.datetime.now()
    reg_info.reg_type = user_pb2.NICK
    user.reg_info = reg_info
    
    if 'ip' in fields and fields['ip'] is not None:
        reg_info.reg_ip = fields['ip']

#try:
    user.save()
    return user
#except:
#return None



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
