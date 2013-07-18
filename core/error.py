# -*- coding: utf-8 -*-

from pbmodels.response_pb2 import *

ERROR_DICT = {

    UNKNOW_ERROR : 'Unknow error!',

    SUCCESS : 'success!',
    SYSTEM_ERROR : 'System error!',
    PARSE_PB_ERROR : 'Parse data error!',
    PARAMETER_ERROR : 'Parameters are null!',
    AUTH_ERROR : 'Pivilege not enough!',
    NETWORK_ERROR : 'Network error!',
    TIMEOUT_ERROR : 'Timeout!',

#User error code: from 10000 to 19999

    USER_NOT_EXISTS_ERROR : 'User not exists!',
    PASSWORD_INCORRECT_ERROR : 'Password is incorrect!',
    USER_STATUS_EXCEPTION_ERROR : 'User status is exception!',

#Action error code: from 20000 to 29999

    ACTION_NOT_EXISTS_ERROR : 'Action not exists!',
    ACTION_STATUS_EXCEPTION_ERROR : 'Action status is exception!',
}

