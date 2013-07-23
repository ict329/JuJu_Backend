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

def _get_follow_relation_list(uid, offset, count):
    uid = ObjectId(uid)
    try:
        relations = Relation.objects(uid=uid, relation=FOLLOW).order_by('-_id')[offset:count]
        log.info('get follow relation len = %d', (len(relations)))
        log.info(relations)
        return relations
    except:
        relations = Relation.objects(uid=uid, relation=FOLLOW).order_by('-_id')
        log.info('get follow except: relation len = %d', (len(relations)))
        log.info(relations)
        return relations

def _get_fan_relation_list(uid, offset, count):
    uid = ObjectId(uid)
    try:
        relations = Relation.objects(fid=uid, relation=FOLLOW).order_by('-_id')[offset:count]
        log.info('get fans relation len = %d', (len(relations)))
        log.info(relations)
        return relations
    except:
        relations = Relation.objects(fid=uid, relation=FOLLOW).order_by('-_id')
        log.info('get fans except: relation len = %d', (len(relations)))
        log.info(relations)
        return relations

def _get_black_relation_list(uid, offset, count):
    uid = ObjectId(uid)
    try:
        return Relation.objects(uid=uid, relation=BLACK).order_by('-_id')[offset:count]
    except:
        return Relation.objects(uid=uid, relation=BLACK).order_by('-_id')
    
########

def _get_follows_from_relations(relations):
    uids = [relation.fid for relation in relations]
    users = user_manager.get_users(uids)
    kv = {}
    for relation in relations:
        kv[relation.fid] = relation
    for user in users:
        relation = kv[relation.fid]
        user.basic_info.mark = relation.mark
        user.reg_info = None
        user.log_info = None
    return users

def _get_fans_from_relations(relations):
    uids = [relation.uid for relation in relations]
    users = user_manager.get_users(uids)
    kv = {}
    for relation in relations:
        kv[relation.uid] = relation
    for user in users:
        relation = kv[relation.uid]
        user.basic_info.mark = relation.mark
        user.reg_info = None
        user.log_info = None
    return users
 

def get_follow_list(uid, offset, count):
    relations = _get_follow_relation_list(uid, offset, count)
    return _get_follows_from_relations(relations)

def get_fan_list(uid, offset, count):
    log.info('uid = %s, offset = %d, count = %d' % (uid, offset, count))
    relations = _get_fan_relation_list(uid, offset, count)
    return _get_follows_from_relations(relations)

def get_black_list(uid, offset, count):
    relations = _get_black_relation_list(uid, offset, count)
    return _get_follows_from_relations(relations)

