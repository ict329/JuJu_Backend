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
    

    def get_field_list(self):
        return ('name')

    def update_pb(self, pb):
        update_pb_with_document(pb, self, self.get_field_list())
        update_pb_with_list(pb, 'image_list', image_list)
        update_pb_with_value(pb, 'album_id', str(self.pk))
        self.user.update_briefuser(pb.user)


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
    site_url = StringField()
    web_url = StringField()
    wap_url = StringField()
    img_url = StringField()

    promotions = ListField(ObjectId)


    def get_field_list(self):
        return ("aibang_id", "name", "county", "addr", "tel",\
                "cate", "rate", "cost", "desc", "lng", "lat", \
                "work_time", "site_url", "web_url", "wap_url", )

    def update_pb(self, pb):
        update_pb_with_document(pb, self, self.get_field_list())
        update_pb_with_value(pb, 'merchant_id', str(self.pk))

        promotion_ids = [str(p_id) for p_id in promotions]
        update_pb_with_list(pb, 'promotion_ids', promotion_ids)


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
    related_action = ReferenceField('self')

class Comment (Document):
    action_id = ObjectId()
    user = ReferenceField(User)
    content = StringField()
    star = IntField()
    is_reply = BooleanField()
    reply_action_id = ObjectId()
    digest = StringField(max_length=80)


