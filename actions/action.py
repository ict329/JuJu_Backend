# -*- coding: utf-8 -*-
# user db model
from mongoengine import *
from pbmodels.user_pb2 import *
from pbmodels.action_pb2 import *
from pbmodels.basic_pb2 import *
from pbmodels.response_pb2 import *
from users.user import *
from bson.objectid import ObjectId

from common.models.basic import *


import constant.db as db
import constant.para as para

class Album(Document):
    user = ReferenceField(User)
    name = StringField(max_length=50)
    image_list = ListField(StringField())

class Merchant(Document):
    aibang_id = StringField(max_length=50)
    name = StringField()
    county = StringField(max_length=50)
    addr = StringField()
    tel = StringField(max_length=50)
    cate = StringField(max_length=50)
    rate = FloatField()
    cost = IntField()
    desc = StringField()
    lng = FloatField()
    lat = FloatField()
    work_time = StringField(max_length=50)
    site_url = URLField()
    web_url = URLField()
    wap_url = URLField()
    img_url = URLField()

    promotions = ListField(ObjectId)

class Promotion(Document):
    start_date = DateTimeField(required=True)
    end_date = DateTimeField(required=True)
    title = StringField()
    content = StringField()
    merchant = ReferenceField(Merchant)


class CommonActivity(EmbeddedDocument):
    token = StringField(max_length=100)
    location = EmbeddedDocumentField(Location)
    contact = EmbeddedDocumentField(Contact)
    join_deadtime = DateTimeField()
    hold_time = DateTimeField()
    content = StringField()
    pay_type = IntField(default=AA)
    budget = IntField()
    price = IntField()
    member_limit = IntField()
    photo_list = ListField(StringField())

    participants = ListField(StringField())
    signups = ListField(StringField())

    comment_count = IntField()
    share_count = IntField()
    signup_count = IntField()
    participant_count = IntField()
    mark_count = IntField()

    meta = {'allow_inheritance': True}


class Party(CommonActivity):
    merchant = ReferenceField(Merchant)
    location = EmbeddedDocumentField(Location)

class Traffic(CommonActivity):
    start_loc = EmbeddedDocumentField(Location)
    end_loc = EmbeddedDocumentField(Location)

class Shopping(CommonActivity):
    merchant = ReferenceField(Merchant)
    location = EmbeddedDocumentField(Location)

class Activity(EmbeddedDocument):
    activity_type = IntField(required=True)
    party = EmbeddedDocumentField(Party)
    traffic = EmbeddedDocumentField(Traffic)
    shopping = EmbeddedDocumentField(Shopping)


class Action(Document):
    action_type = IntField(required=True)
    user = ReferenceField(User)
    activity = EmbeddedDocumentField(Activity) #if type is activity
    action_id = ObjectId() #if type is share or join
    related_action = ReferenceField('self')

class Comment (Document):
    action= ReferenceField(Action)
    user = ReferenceField(User)
    content = StringField()
    star = IntField()
    is_reply = BooleanField()
    reply_action = ReferenceField(Action) 
    digest = StringField(max_length=80)


