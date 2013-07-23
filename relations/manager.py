# -*- coding: utf-8 -*-
# -*- 2013-07-20 -*-

from relations.relation import *
from pbmodels.user_pb2 import *
from bson.objectid import ObjectId
import users.manager as user_manager
import datetime


def _get_relation(uid, fid):
    uid = ObjectId(uid)
    fid = ObjectId(fid)
    try:
        return Relation.objects.get(uid=uid, fid=fid)
    except:
        return STRANGE 

def _set_relation(uid, fid, relation):
    uid = ObjectId(uid)
    fid = ObjectId(fid)
    Relation.objects(uid=uid,fid=fid).update_one(set__relation=relation, \
            set__c_date=datetime.datetime.utcnow(), upsert=True) 
    

def follow(uid, fid):
    _set_relation(uid, fid, FOLLOW) 
    user_manager.inc(uid, {'follow_count':1})
    user_manager.inc(fid, {'fan_count':1, 'new_fan_count':1})


def black(uid, fid):
    relation = _get_relation(uid, fid)
    if relation.relation == FOLLOW:
        user_manager.inc(uid, {'follow_count': -1})
        user_manager.inc(fid, {'fan_count':-1, 'new_fan_count':-1})
    relation.relation = BLACK
    relation.c_date = datetime.datetime.utcnow()
    relation.save()

def unfollow(uid, fid):
    _set_relation(uid, fid, STRANGE)
    user_manager.inc(uid, {'follow_count': -1})
    user_manager.inc(fid, {'fan_count':-1, 'new_fan_count':-1})

def mark_friend(uid, fid, mark):
    Relation.objects(uid=uid, fid=fid).update_one(set__mark=mark)

def relation_between(uid1, uid2):
    return _get_relation(uid1, uid2) | _get_relation(uid2,uid1)

def _c_date(c_date):
    if not c_date:
        c_date = datetime.datetime.utcnow()
    return c_date

def _get_follow_relation_list(uid, c_date, count):
    try:
        return Relation.objects(uid=uid, relation=FOLLOW, c_date__lt=_c_date(c_date)).order_by('-c_date')[0:count]
    except:
        return Relation.objects(uid=uid, relation=FOLLOW, c_date__lt=_c_date(c_date)).order_by('-c_date')

def _get_fan_relation_list(uid, c_date, count):
    try:
        return Relation.objects(fid=uid, relation=FOLLOW, c_date__lt=_c_date(c_date)).order_by('-c_date')[0:count]
    except:
        return Relation.objects(fid=uid, relation=FOLLOW, c_date__lt=_c_date(c_date)).order_by('-c_date')

def _get_black_relation_list(uid, c_date, count):
    try:
        return Relation.objects(uid=uid, relation=BLACK, c_date__lt=_c_date(c_date)).order_by('-c_date')[0:count]
    except:
        return Relation.objects(uid=uid, relation=BLACK, c_date__lt=_c_date(c_date)).order_by('-c_date')
    
########

def _get_users_from_relations(relations):
    uids = [user.pk for user in relations]
    users = user_manager.get_users(uids)
    kv = {}
    for relation in relations:
        kv[relation.pk] = relation
    for user in users:
        relation = kv[relation.pk]
        user.basic_info.mark = relation.mark
    return users
    

def get_follow_list(uid, c_date, count):
    relations = _get_follow_relation_list(uid, c_date, count)
    return _get_users_from_relations(relations)

def get_fan_list(uid, c_date, count):
    relations = _get_fan_relation_list(uid, c_date, count)
    return _get_users_from_relations(relations)

def get_black_list(uid, c_date, count):
    relations = _get_black_relation_list(uid, c_date, count)
    return _get_users_from_relations(relations)

