# -*- coding: utf-8 -*-
# -*- 2013-08-13 -*-

def create_activity(uid, **paras):

    #TODO set data

    #TODO save data

    #TODO update count

    #TODO update timeline of fans

    pass

def edit_activity(uid, action_id, **paras):
    pass

def delete_activity(uid, action_id, **paras):

    #TODO set delete flag

    #TODO update count

    pass

def share_action(uid, action_id, comment):
    pass

def get_user_actions(uid,offset,count, **paras):
    #TODO get actions 
    return None

def get_nearby_actions(lat, lng, distance, offset, count, **paras):
    #TODO get actions 
    return None

def get_sigup_actions(uid, offset, count, **paras):
    return None

def get_join_actions(uid, offset, count, **paras):
    return None

def get_favor_actions(uid, offset, count, **paras):
    return None

def get_timeline(uid, offset, count, **paras):
    return None


#comment functions

def comment_action(uid, action_id, comment, **paras):
    return None

def delete_comment(uid, comment_id):
    return None

def get_action_comments(action_id, offset, count, **paras):
    return None

def get_received_comments(uid, offset, count, **paras):
    return None 
