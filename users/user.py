# -*- coding: utf-8 -*-
# user db model
from mongoengine import *

class UserBasic(EmbeddedDocument):
    uname = StringField(max_length=50, required=True, unique = True)
    nick = StringField(max_length=50, required=True)
    role = IntField()
    gender = BooleanField()
    avatar = StringField()
    status = IntField()
    introduction = StringField()
    birth_date = DateTimeField()
    tags = ListField(StringField())

class SNS(EmbeddedDocument):
    tel_number = StringField(max_length=50)
    qq_number = StringField(max_length=50)
    qq_weibo_id = StringField(max_length=50)
    qq_weibo_nick = StringField(max_length=50)
    sina_weibo_id = StringField(max_length=50)
    sina_weibo_nick = StringField(max_length=50)
    renren_id = StringField(max_length=50)
    renren_nick = StringField(max_length=50)

class Log(EmbeddedDocument):
    last_log_date = DateTimeField()
    last_log_ip = IntField()
    last_log_latitude = FloatField()
    last_log_longitude = FloatField()

class Statistic(EmbeddedDocument):
    fan_count = IntField()
    follow_count = IntField()
    my_activity = IntField()

class Device(EmbeddedDocument):
    device_id = StringField(max_length=50, required=True)
    device_os = StringField(max_length=50, required=True)
    device_token = StringField(max_length=50, required=True)
    device_name = StringField(max_length=50, required=True)

class Registion(EmbeddedDocument):
    reg_date = DateTimeField(required=True)
    reg_type = IntField(default=1)
    reg_ip = IntField()

class User(Document):
    basic_info = EmbeddedDocumentField(UserBasic, required=True)
    registion = EmbeddedDocumentField(Registion)
    device_info = EmbeddedDocumentField(Device)
    log_info = EmbeddedDocumentField(Log)
    sns_info = EmbeddedDocumentField(SNS)
    statistic = EmbeddedDocumentField(Statistic)
