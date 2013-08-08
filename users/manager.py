#-*- coding: utf-8 -*-
# -*- 2013-07-16 -*-

from users.user import *
import datetime
import pbmodels.user_pb2 as PBUser 
import constant.para as para
from bson import ObjectId
import logging


log = logging.getLogger('UserManager')


def _set_value(dist, attr, src, field, nil_value):
    try: 
        value = src[field]
        if value != nil_value:
            setattr(dist, attr, value)
    except:
        pass


def _get_value_with_field(info, field):
    try:
        return info[field]
    except Exception, e:
        log.info("_get_value_with_field exception: " + e)
        return None

def _update_log_info(log_info, info):
    _set_value(log_info, 'last_log_ip', info, para.IP, None)
    
    lat = _get_value_with_field(info, para.LATITUDE)
    lng = _get_value_with_field(info, para.LONGITUDE)

    if lat and lng:
        log_info.location = [lat, lng]

    log_info.last_log_date = datetime.datetime.utcnow()


def _update_device_info(device_info, info):
    _set_value(device_info, 'device_id', info, para.DEVICE_ID, None)
    _set_value(device_info, 'device_os', info, para.DEVICE_OS, None)
    _set_value(device_info, 'device_name', info, para.DEVICE_NAME, None)
    _set_value(device_info, 'device_token', info, para.DEVICE_TOKEN, None)
      
def _update_user_device_log_info(user, args):
    if user.log_info is None:
        user.log_info = Log()
    _update_log_info(user.log_info, args)

    if user.device_info is None:
        user.device_info = Device()
    _update_device_info(user.device_info, args)


def update_profile(uid, **profile):
    user = get_user(self.uid)
    if user:
        _set_value(user, 'nick', profile, para.NICK, None)
        _set_value(user, 'password', profile, para.NEW_PASSWORD, None)
        _set_value(user, 'gender', profile, para.GENDER, None)
        _set_value(user, 'status', profile, para.STATUS, 0)
        _set_value(user, 'introduction', profile, para.INTRODUCTION, None)
        _set_value(user, 'birth_date', profile, para.BIRTH_DATE, None)
        _set_value(user, 'tags', profile, para.TAGS, None)
        _set_value(user, 'avatar', profile, para.AVATAR, None)
        _set_value(user, 'city', profile, para.CITY, None)
        user.save()
    return user

def login(uname, password, **args):
    user = User.objects.get(basic_info__uname = uname, basic_info__password = password)
    _update_user_device_log_info(user, args)
    user.save()
    return user

def get_user(uid):
    try:
        if type(uid) == str:
            uid = ObjectId(uid)
        return User.objects.get(pk=uid)
    except:
        return None

def get_user_by_uname(uname):
    try:
        return User.objects.get(basic_info__uname = uname)
    except:
        return None

def get_users(uids):
    try:
        if type(uids[0]) == str:
            uids = [ObjectId(uid) for uid in uids]
        users = User.objects(pk__in=uids)
        return users
    except:
        return [] 

def register(uname, password, **args):
    user = User()
    
    basic = UserBasic()
    basic.uname = uname
    basic.password = password
    basic.nick = uname
    user.basic_info = basic

    reg_info = Registration()
    user.reg_info = reg_info
    
    reg_info.reg_date = datetime.datetime.utcnow()
    reg_info.reg_type = PBUser.NICK
    _set_value(reg_info, 'reg_ip', args, para.IP, None)

    _update_user_device_log_info(user, args)

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
    reg.reg_date = datetime.datetime.utcnow()
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
   
    _update_user_device_log_info(user, args)

    user.save()

    return user

#all the kv must in statistic
def inc(uid, kv, min_value = 0):
    user = get_user(uid)
    if user.statistic is None:
        user.statistic = Statistic()
    stat = user.statistic

    for k,v in kv.items():
        origin = 0
        if hasattr(stat, k):
            origin = getattr(stat, k)
            if not origin:
                origin = 0
        setattr(stat, k, max(origin + v, min_value))
    user.save()
