# -*- coding: utf-8 -*-
# -*- 2013-07-20 -*-

from relations.relation import *
from pbmodels.user_pb2 import *
from bson.objectid import ObjectId
import users.manager as user_manager
import datetime
import logging

log=logging.getLogger('RelationManager')


def _get_relation(uid, fid):
    try:
        user = User(pk=uid)
        friend = User(pk=fid)
        return Relation.objects.get(user=user,friend=friend)
    except:
        return None

def _set_relation(uid, fid, relation):
    user = User(pk=uid)
    friend = User(pk=fid)
    Relation.objects(user=user, friend=friend).update_one(set__relation=relation, \
            set__c_date=datetime.datetime.utcnow(), upsert=True) 
    

def follow(uid, fid):
    relation = _get_relation(uid, fid)
    if not relation or relation.relation != FOLLOW:
        _set_relation(uid, fid, FOLLOW) 
        user_manager.inc(uid, {'follow_count':1})
        user_manager.inc(fid, {'fan_count':1, 'new_fan_count':1})


def black(uid, fid):
    relation = _get_relation(uid, fid)
    if relation.relation == FOLLOW:
        user_manager.inc(uid, {'follow_count': -1})
        user_manager.inc(fid, {'fan_count':-1})
    relation.relation = BLACK
    relation.c_date = datetime.datetime.utcnow()
    relation.save()

def unfollow(uid, fid):
    relation = _get_relation(uid, fid)
    if relation and relation.relation == FOLLOW:
        _set_relation(uid, fid, STRANGE)
        user_manager.inc(uid, {'follow_count': -1})
        user_manager.inc(fid, {'fan_count':-1})

def unblack(uid, fid):
    relation = _get_relation(uid, fid)
    if relation and relation.relation == BLACK:
        _set_relation(uid, fid, STRANGE)

def mark_friend(uid, fid, mark):
    user = User(pk=uid)
    friend = User(pk=fid)
    Relation.objects(user=user, friend=friend).update_one(set__mark=mark)

def relation_between(uid1, uid2):
    r1 = _get_relation(uid1, uid2)
    r2 = _get_relation(uid2, uid1)
    f = lambda x: [STRANGE, x.relation][x is None]
    return f(r1) | f(r2)

def _get_follow_relation_list(uid, offset, count):
    try:
        relations = Relation.objects(user=User(pk=uid), relation=FOLLOW).order_by('-_id')[offset:count]
        return relations
    except:
        relations = Relation.objects(user=User(pk=uid), relation=FOLLOW).order_by('-_id')[offset:]
        return relations

def _get_fan_relation_list(uid, offset, count):
    try:
        relations = Relation.objects(friend=User(pk=uid), relation=FOLLOW).order_by('-_id')[offset:count]
        return relations
    except:
        relations = Relation.objects(friend=User(pk=uid), relation=FOLLOW).order_by('-_id')[offset:]
        return relations

def _get_black_relation_list(uid, offset, count):
    try:
        relations = Relation.objects(user=User(pk=uid), relation=BLACK).order_by('-_id')[offset:count]
        return relations
    except:
        relations = Relation.objects(user=User(pk=uid), relation=BLACK).order_by('-_id')[offset:]
        return relations
    
########

def _update_mark(relations):
    for relation in relations:
        relation.friend.mark = relation.mark

def get_follow_list(uid, offset, count):
    relations = _get_follow_relation_list(uid, offset, count)
    _update_mark(relations)
    return [relation.friend for relation in relations]

def get_fan_list(uid, offset, count):
    relations = _get_fan_relation_list(uid, offset, count)
    return [relation.user for relation in relations]

def get_black_list(uid, offset, count):
    relations = _get_black_relation_list(uid, offset, count)
    return [relation.friend for relation in relations]
