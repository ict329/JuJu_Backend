#-*- coding: utf-8 -*-
# -*- 2013-07-16 -*-

from users.user import *
import datetime
import pbmodels.user_pb2 as PBUser 
import constant.para as para
from bson import ObjectId
import logging


log = logging.getLogger('UserManager')

def _get_value_with_field(info, field):
    if field in info and info[field] is not None:
        return info[field]
    return None

def _update_log_info(log_info, info):
    value = _get_value_with_field(info, para.IP)
    if value is not None:
        log_info.last_log_ip = value
    
    value = _get_value_with_field(info, para.LATITUDE)
    if value != 0.0:
        log_info.last_log_latitude = value
    
    value = _get_value_with_field(info, para.LONGITUDE)
    if value != 0.0:
        log_info.last_log_longitude = value
    
    log_info.last_log_date = datetime.datetime.now()
"""
    device_id = StringField(max_length=50, required=True)
    device_os = StringField(max_length=50, required=True)
    device_token = StringField(max_length=50, required=True)
    device_name = StringField(max_length=50, required=True)
"""
def _update_device_info(device_info, info):
    value = _get_value_with_field(info, para.DEVICE_ID)
    if value is not None:
        device_info.device_id = value
    
    value = _get_value_with_field(info, para.DEVICE_OS)
    if value is not None:
        device_info.device_os = value
    
    value = _get_value_with_field(info, para.DEVICE_TOKEN)
    if value is not None:
        device_info.device_token = value
    
    value = _get_value_with_field(info, para.DEVICE_NAME)
    if value is not None:
        device_info.device_name = value

def login(uname, password, **args):
    user = User.objects.get(basic_info__uname = uname, basic_info__password = password)
    if user.log_info is None:
        user.log_info = Log()
    _update_log_info(user.log_info, args)

    if user.device_info is None:
        user.device_info = Device()
    _update_device_info(user.device_info, args)

    user.save()

    return user

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

def register(uname, password, **args):
    user = User()
    
    basic = UserBasic()
    basic.uname = uname
    basic.password = password
    basic.nick = uname
    user.basic_info = basic

    reg_info = Registration()
    reg_info.reg_date = datetime.datetime.now()
    reg_info.reg_type = PBUser.NICK
    ip = _get_value_with_field(args, para.IP)

    user.reg_info = reg_info
     
    if user.log_info is None:
        user.log_info = Log()
    _update_log_info(user.log_info, args)

    if user.device_info is None:
        user.device_info = Device()
    _update_device_info(user.device_info, args)

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
    reg.reg_ip = ip
    
    user = User()
    user.basic_info = basic
    user.reg_info = reg
    user.sns_info = sns
#    user.save()
    return user


def snslogin(sns_type, sns_id, sns_token, sns_nick, **args):
    user = get_user_with_sns(sns_type, sns_id)

    if user is None:
        ip = _get_value_with_field(args, para.IP) 
        user = _add_user_with_sns(sns_type, sns_id, sns_token, sns_nick, ip)
    
    if user.log_info is None:
        user.log_info = Log()
    _update_log_info(user.log_info, args)

    if user.device_info is None:
        user.device_info = Device()
    _update_device_info(user.device_info, args)

    user.save()

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
