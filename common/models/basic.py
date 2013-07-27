# -*- coding: utf-8 -*-
# -*- 2013-07-27 -*-

from mongoengine import *

class Location(EmbeddedDocument):
    country_code = IntField(required=True)
    province = StringField(required=True)
    city = StringField(required=True)
    position = PointField(auto_index=True)

class Contact(EmbeddedDocument):
    tel_numbers = ListField(StringField)
