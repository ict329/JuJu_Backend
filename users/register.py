# -*- coding: utf-8 -*-
from flask import request
import logging

#from utils import *
#from constants import * 
from core.service import JJService

from users.user import User

import users.manager as user_manager
import common.utils.request_util as request_util 
import constant.para as para

class RegisterService(JJService):

    log = logging.getLogger('RegisterService')

    def __init__(self, request):
        self.request = request


    #protected methods, to be override
    def _parse_request(self):
        self.uname =  request_util.get_value(self.request, para.UNAME)
        self.password = request_util.get_value(self.request, para.PASSWORD) 
        self.ip = request.remote_addr

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
#TODO try to catch the exception and return the error response

        user = user_manager.register(self.uname, self.password, ip=request.remote_addr)
        pbuser = user.build_pb()
        return pbuser.SerializeToString()
        
    def _handle_error(self):
        return JJService._handle_error(self)


