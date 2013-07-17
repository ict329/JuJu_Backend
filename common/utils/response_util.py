# -*- coding: utf-8 -*-
# -*- 2013-07-16 -*-

from pbmodels.response_pb2 import *
from core.error import ERROR_DICT

def get_error_response(code, error_message = None):
    response = PBResponse()
    response.code = code
    if error_message is None:
        if code in ERROR_DICT:
            response.error_message = ERROR_DICT[code]
        else:
            response.error_message = ERROR_DICT[UNKNOW_ERROR]
    else:
        response.error_message = error_message
    return response

