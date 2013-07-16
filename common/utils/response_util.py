# -*- coding: utf-8 -*-
# -*- 2013-07-16 -*-

from pbmodels.response_pb2 import *


def get_error_response(code, error_message):
    response = PBResponse()
    response.code = code
    if error_message is not None:
        response.error_message = error_message
    return response

