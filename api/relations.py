# -*- coding: utf-8 -*-

"""
    Relation related api
"""
from flask import Blueprint, request
from services import *

bp = Blueprint('relations', __name__, url_prefix='/api/relations')

@bp.route('/follow')
def follow():
    return FollowUserService(request).handle()

@bp.route('/unfollow')
def unfollow():
    return UnfollowUserService(request).handle()

@bp.route('/black')
def black():
    return BlackUserService(request).handle()

@bp.route('/mark')
def mark():
    return MarkFriendService(request).handle()

@bp.route('/getfans')
def getfans():
    return GetFansService(request).handle()

@bp.route('/getfollows')
def getfollows():
    return GetFollowsService(request).handle()
