# -*- coding: utf-8 -*-
# user db model
from mongoengine import *
from pbmodels.basic_pb2 import *
from pbmodels.user_pb2 import *
from utils import *
from utils import *



class UserBasic(EmbeddedDocument):
    uname = StringField(max_length=50, required=True, unique = True)
    nick = StringField(max_length=50, required=True)
    password = StringField(max_length=50)
    role = IntField()
    gender = BooleanField()
    avatar = StringField()
    status = IntField()
    introduction = StringField()
    birth_date = DateTimeField()
    tags = ListField(StringField())

    def get_field_list(self):
        return ('uname', 'nick', 'role', 'gender', 'avatar', 'status','introduction')

    def update_pb(self, basic_info):
        update_pb_with_document(basic_info, self, self.get_field_list())
        update_pb_with_value(basic_info, 'birth_date', datetime_to_timestamp(self.birth_date))
        update_pb_with_list(basic_info, 'tags', self.tags)

class SNS(EmbeddedDocument):
    tel_number = StringField(max_length=50)
    qq_number = StringField(max_length=50)
    qq_weibo_id = StringField(max_length=50)
    qq_weibo_nick = StringField(max_length=50)
    qq_weibo_token = StringField(max_length=50)
    
    sina_weibo_id = StringField(max_length=50)
    sina_weibo_nick = StringField(max_length=50)
    sina_weibo_token = StringField(max_length=50)
    renren_id = StringField(max_length=50)
    renren_nick = StringField(max_length=50)
    renren_token = StringField(max_length=50)
    
    def get_field_list(self):
        return ('tel_number', 'qq_number', 'qq_weibo_id', 'qq_weibo_nick', 'sina_weibo_id', 'sina_weibo_nick','renren_id', 'renren_nick')

    def update_pb(self, sns):
        update_pb_with_document(sns, self, self.get_field_list())

class Log(EmbeddedDocument):
    last_log_date = DateTimeField()
    last_log_ip = StringField()
    last_log_latitude = FloatField()
    last_log_longitude = FloatField()
    
    def get_field_list(self):
        return ('last_log_ip', 'last_log_latitude', 'last_log_longitude')

    def update_pb(self, log_info):
        update_pb_with_document(log_info, self, self.get_field_list())
        update_pb_with_value(log_info, 'last_log_date', datetime_to_timestamp(self.last_log_date))

class Statistic(EmbeddedDocument):
    fan_count = IntField()
    follow_count = IntField()
    my_activity = IntField()
    
    new_fan_count = IntField()
    new_follow_count = IntField()
    new_message_count = IntField()
    new_feed_count= IntField()
    new_notice_count= IntField()

    def get_field_list(self):
        return ('my_activity', 'fan_count', 'follow_count', \
                'new_fan_count', 'new_follow_count', \
                'new_message_count', 'new_feed_count', \
                'new_notice_count')

    def update_pb(self, statistic):
        update_pb_with_document(statistic, self, self.get_field_list())

class Device(EmbeddedDocument):
    device_id = StringField(max_length=50)
    device_os = StringField(max_length=50)
    device_token = StringField(max_length=50)
    device_name = StringField(max_length=50)
    
    def get_field_list(self):
        return ('device_id', 'device_os', 'device_token', 'device_name')

    def update_pb(self, device_info):
        update_pb_with_document(device_info, self, self.get_field_list())

class Registration(EmbeddedDocument):
    reg_date = DateTimeField(required=True)
    reg_type = IntField(default=1)
    reg_ip = StringField()
    def get_field_list(self):
        return ('reg_type', 'reg_ip')

    def update_pb(self, reg_info):
        update_pb_with_document(reg_info, self, self.get_field_list())
        update_pb_with_value(reg_info, 'reg_date', datetime_to_timestamp(self.reg_date))

class User(Document):
    basic_info = EmbeddedDocumentField(UserBasic, required=True)
    reg_info = EmbeddedDocumentField(Registration)
    device_info = EmbeddedDocumentField(Device)
    log_info = EmbeddedDocumentField(Log)
    sns_info = EmbeddedDocumentField(SNS)
    statistic = EmbeddedDocumentField(Statistic)


    def get_field_list(self):
        return ('basic_info', 'reg_info', 'device_info', 'log_info', 'sns_info','statistic')

    def update_pb(self, user):
        if self.basic_info is not None:
            self.basic_info.update_pb(user.basic_info) 
        if self.reg_info is not None:
            self.reg_info.update_pb(user.reg_info)
        if self.device_info is not None:
            self.device_info.update_pb(user.device_info)
        if self.log_info is not None:
            self.log_info.update_pb(user.log_info)
        if self.sns_info is not None:
            self.sns_info.update_pb(user.sns_info)
        if self.statistic is not None:
            self.statistic.update_pb(user.statistic)
        if self.pk is not None:
            user.uid = str(self.pk)


    def build_pb(self):
        user = PBUser()
        self.update_pb(user)
        return user
