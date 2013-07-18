# -*- coding: utf-8 -*-

"""
    对外暴露的统一的服务模块，用于注册所有服务,api层只要引入这个文件即可
"""

from users.user_service import UserService
from users.bind_sns import BindSNSService
from users.get_profile import GetProfileService
from users.login import LoginService
from users.snslogin import SNSLoginService
from users.logout import LogoutService
from users.register import RegisterService
from users.update_device import UpdateDeviceService
from users.update_profile import UpdateProfileService

from actions.comment_action import CommentActionService
from actions.create_activity import CreateActivityService
from actions.delete_action import DeleteActionService
from actions.delete_comment import DeleteCommentService
from actions.get_actions import GetActionsService
from actions.get_comments import GetCommentsService
from actions.get_timeline import GetTimelineService
from actions.share_action import ShareActionService

from relations.black_user import BlackUserService
from relations.follow import FollowUserService
from relations.get_follows import GetFollowsService
from relations.get_follows import GetFollowsService
from relations.mark_friend import MarkFriendService
from relations.unfollow import UnfollowUserService
