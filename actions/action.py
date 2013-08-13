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

        if self.promotions:
            promotion_ids = [str(p_id) for p_id in self.promotions]
            update_pb_with_list(pb, 'promotion_ids', promotion_ids)


class Promotion(Document):
    start_date = DateTimeField(required=True)
    end_date = DateTimeField(required=True)
    title = StringField()
    content = StringField()
    merchant_id = ObjectIdField()

    def get_field_list(self):
        return ("promotion_id","title","content","status",)

    def update_pb(self, pb):
        update_pb_with_document(pb, self, self.get_field_list())

        update_pb_with_value(pb, 'merchant_id', str(self.merchant_id))
        update_pb_with_value(pb, 'promotion_id', str(self.pk))
        update_pb_with_value(pb, 'start_date', datetime_to_timestamp(self.start_date))
        update_pb_with_value(pb, 'end_date', datetime_to_timestamp(self.end_date))

class CommonActivity(EmbeddedDocument):

    token = StringField(max_length=100)
    content = StringField()
    pay_type = IntField(default=AA)
    budget = IntField()
    price = IntField()
    member_limit = IntField()

    join_deadtime = DateTimeField()
    hold_time = DateTimeField()

    contact = EmbeddedDocumentField(Contact)

    photo_list = ListField(StringField())
    participants = ListField(ObjectIdField())
    signups = ListField(ObjectIdField())

    comment_count = IntField()
    share_count = IntField()
    signup_count = IntField()
    participant_count = IntField()
    mark_count = IntField()

    meta = {'allow_inheritance': True}


    def get_field_list(self):
        return ("token", "pay_type", "budget", "price", "member_limit",\
            "comment_count", \
            "share_count", "participant_count", "mark_count", \
            "join_deadtime", "hold_deadtime", "merchant", "start_loc", "end_loc",)

    def update_pb(self, pb):
        if not pb:
            return
        update_pb_with_document(pb, self, self.get_field_list())
        update_pb_with_value(pb, 'join_deadtime', datetime_to_timestamp(self.join_deadtime))
        update_pb_with_value(pb, 'hold_time', datetime_to_timestamp(self.hold_time))
        update_pb_with_list(pb, 'photo_list', self.photo_list)

        if self.participants: 
            participant_ids = [str(p_id) for p_id in self.participants]
            update_pb_with_list(pb, 'participants', participant_ids)
        
        if self.signups:
            signup_ids = [str(s_id) for s_id in self.signups]
            update_pb_with_list(pb, 'signups', signup_ids)

        if self.location:
            self.location.update_pb(pb.location)

        if self.contact:
            self.concat.update_pb(pb.contact)
        

class Party(CommonActivity):
    merchant = ReferenceField(Merchant)
    location = EmbeddedDocumentField(Location)

    def update_pb(self, pb):
        if not pb:
            return
        pb.type = PARTY
        CommonActivity.update_pb(self, pb)
        if self.location:
            self.location.update_pb(pb.location)
        if self.merchant:
            self.merchant.update_pb(pb.merchant)

class Traffic(CommonActivity):
    start_loc = EmbeddedDocumentField(Location)
    end_loc = EmbeddedDocumentField(Location)

    def update_pb(self, pb):
        if not pb:
            return
        pb.type = TRAFFIC 
        CommonActivity.update_pb(self, pb)
        if self.start_loc:
            self.start_loc.update_pb(pb.start_loc)

        if self.end_loc:
            self.end_loc.update_pb(pb.end_loc)

class Shopping(CommonActivity):
    merchant = ReferenceField(Merchant)
    location = EmbeddedDocumentField(Location)

    def update_pb(self, pb):
        if not pb:
            return
        pb.type = SHOPPING
        CommonActivity.update_pb(self, pb)
        if self.location:
            self.location.update_pb(pb.location)
        if self.merchant:
            self.merchant.update_pb(pb.merchant)

class Activity(EmbeddedDocument):
    activity_type = IntField(required=True)
    party = EmbeddedDocumentField(Party)
    traffic = EmbeddedDocumentField(Traffic)
    shopping = EmbeddedDocumentField(Shopping)
    
    def update_pb(self, pb):
        if pb:
            if action_type == PARTY and self.party:
                self.party.update_pb(pb)
                
            if action_type == TRAFFIC and self.traffic:
                self.traffic.update_pb(pb)

            if action_type == SHOPPING and self.shopping:
                self.shopping.update_pb(pb)


class Action(Document):
    action_type = IntField(required=True)
    user = ReferenceField(User)
    activity = EmbeddedDocumentField(Activity) #if type is activity
    related_action = ReferenceField('self')

    def update_pb(self, pb):
        if pb:
            update_pb_with_value(pb, 'type', self.action_type)
            update_pb_with_value(pb, 'action_id', str(pk))
            update_pb_with_value(pb, 'comment', self.comment)

            c_date = self.pk.generation_time
            update_pb_with_value(pb, 'c_date', datetime_to_timestamp(c_date))

            if self.user:
                self.user.update_briefuser(pb.user)
            if self.activity:
                self.activity.update_pb(pb.activity)

#TODO check point to self reference field
            if self.related_action:
                self.related_action.update_pb(pb.related_action)


class Comment (Document):
    action_id = ObjectId()
    user = ReferenceField(User)

    content = StringField()
    star = IntField()
    is_reply = BooleanField()
    digest = StringField(max_length=80)

    reply_action_id = ObjectId()
    
    def get_field_list(self):
        return ("content", "star", "is_reply", "digest",)

    def update_pb(self, pb):
        update_pb_with_document(pb, self, self.get_field_list())
        update_pb_with_value(pb, 'comment_id', str(self.pk))

        if self.action_id:
            update_pb_with_value(pb, 'action_id', str(self.action_id))
        if self.user:
            self.user.update_briefuser(pb.user)

        c_date = self.pk.generation_time
        update_pb_with_value(pb, 'c_date', datetime_to_timestamp(c_date))


