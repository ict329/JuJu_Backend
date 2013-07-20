# -*- coding: utf-8 -*-
# -*- 2013-07-20 -*-

from relations.relation import *
from pbmodels.user_pb2 import *
from bson.objectid import ObjectId

def _set_relation(uid, fid, relation):
    uid = ObjectId(uid)
    fid = ObjectId(fid)
    Relation.objects(uid=uid,fid=fid).update_one(set__relation=relation, set__c_date=datetime.datetime.now(), upsert=True) 
    

def follow(uid, fid):
    _set_relation(uid, fid, FOLLOW)

def black(uid, fid):
    _set_relation(uid, fid, BLACK)

def unfollow(uid, fid):
    _set_relation(uid, fid, STRANGE)
