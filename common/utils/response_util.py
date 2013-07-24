# -*- coding: utf-8 -*-
# -*- 2013-07-16 -*-

from pbmodels.response_pb2 import *
from core.error import ERROR_DICT


def get_error_response(code, error_message = None):
    response = PBResponse()
    response.code = code

    if error_message:
        response.error_message = error_message
    else:
        response.error_message = ERROR_DICT.get(code, ERROR_DICT[UNKNOW_ERROR])
    return response

def update_users(res, users):
    res.code = SUCCESS
    if not users:
        return
    for user in users:
        pbuser = res.users.add()
        user.update_pb(pbuser)


SUCCESS_RESPONSE = get_error_response(SUCCESS)
UNKNOW_ERROR_RESPONSE = get_error_response(UNKNOW_ERROR)
