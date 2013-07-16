# -*- coding: utf-8 -*-
from common.utils.str_util import *
from common.utils.request_util import get_value
import logging

from core.service import JJService

from flask import request
from constant.service_constant import ARGS
from users.user import User
from users.user_manager import register


class RegisterService(JJService):

    log = logging.getLogger('JJService')

    def __init__(self, request):
        self.request = request


    #protected methods, to be override
    def _parse_request(self):
        self.uname = get_value(self.request, 'uname')
        self.password = get_value(self.request, 'password')

        return True

    def _check_parameters(self):
        if self.uname is None:
            return False
        if self.password is None:
            return False
        return True

    def _authenticate(self):
        return True

    def _handle_data(self):
        user = register(self.uname, self.password)
        pbuser = user.build_pb()
        return pbuser.SerializeToString()
        
    def _handle_error(self):
        return JJService._handle_error(self)

