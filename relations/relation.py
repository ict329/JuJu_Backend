# -*- coding: utf-8 -*-
# -*- 2013-07-20 -*-
# relation db model
from mongoengine import *
from pbmodels.user_pb2 import *
from users.user import *

class Relation(Document):
    user = ReferenceField(User)
    friend = ReferenceField(User)
    relation = IntField(required = True)
    c_date = DateTimeField()
    mark = StringField(max_length = 50)
