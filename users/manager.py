#-*- coding: utf-8 -*-
# -*- 2013-07-16 -*-

from users.user import *
import datetime
import pbmodels.user_pb2 as PBUser 
import constant.para as para
from bson import ObjectId


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
    reg_info.reg_type = PBUser.NICK
    user.reg_info = reg_info
    
    if 'ip' in fields and fields['ip'] is not None:
        reg_info.reg_ip = fields['ip']
    user.save()
    return user

def get_user_with_sns(sns_type, sns_id):
    try:
        if sns_type == PBUser.SINA_WEIBO:
            return User.objects.get(sns_info__sina_weibo_id = sns_id)
        elif sns_type == PBUser.QQ_WEIBO:
            return User.objects.get(sns_info__qq_weibo_id = sns_id)
        elif sns_type == PBUser.RENREN:
            return User.objects.get(sns_info__renren_id = sns_id)
        else:
            return None
    except:
        return None 


def _add_user_with_sns(sns_type, sns_id, sns_token, sns_nick, ip):

# set sns info
    sns = SNS() 
    if sns_type == PBUser.SINA_WEIBO:
        sns.sina_weibo_id = sns_id
        sns.sina_weibo_nick = sns_nick
        sns.sina_weibo_token = sns_token
    elif sns_type == PBUser.QQ_WEIBO:
        sns.qq_weibo_id = sns_id
        sns.qq_weibo_nick = sns_nick
        sns.qq_weibo_token = sns_token
    elif sns_type == PBUser.RENREN:
        sns.renren_id = sns_id
        sns.renren_nick = sns_nick
        sns.renren_token = sns_token
    else:
        pass

# set basic info

    basic = UserBasic()
    basic.nick = sns_nick
    basic.uname = str(ObjectId()) 
    basic.password = ''

# set reg info

    reg = Registration()
    reg.reg_date = datetime.datetime.now()
    reg.reg_type = sns_type
    
    user = User()
    user.basic_info = basic
    user.reg_info = reg
    user.sns_info = sns
    user.save()
    return user


def snslogin(sns_type, sns_id, sns_token, sns_nick, **args):
    user = get_user_with_sns(sns_type, sns_id)
    if user is None:
        ip = None
        if 'ip' in args:
            ip = args['ip']
        user = _add_user_with_sns(sns_type, sns_id, sns_token, sns_nick, ip)
    return user

##### TEST CODE BELOW ######

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
