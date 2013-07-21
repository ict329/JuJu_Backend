# -*- coding: utf-8 -*-
from flask import request
import logging

#from utils import *
#from constants import * 
from core.service import JJService

from users.user import User
from pbmodels.response_pb2 import *

import users.manager as user_manager
import common.utils.request_util as request_util
import common.utils.str_util as str_util
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

        self.latitude = request_util.get_value(self.request, para.LATITUDE)
        self.latitude = str_util.get_float_value(self.latitude)
        self.longitude = request_util.get_value(self.request, para.LONGITUDE)
        self.longitude = str_util.get_float_value(self.longitude)
        self.ip = self.request.remote_addr

        self.device_id = request_util.get_value(self.request, para.DEVICE_ID)
        self.device_os = request_util.get_value(self.request, para.DEVICE_OS)
        self.device_name = request_util.get_value(self.request, para.DEVICE_NAME)
        self.device_token = request_util.get_value(self.request, para.DEVICE_TOKEN)

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

        user = user_manager.register(self.uname, self.password, \
                ip=self.ip, latitude=self.latitude, longitude=self.longitude, \
                device_id=self.device_id, device_name=self.device_name, 
                device_os=self.device_os, device_token=self.device_token)
        self.session['uid'] = str(user.pk)
        rep = PBResponse()
        rep.code = SUCCESS
        user.update_pb(rep.user)
        return rep.SerializeToString()

    def _handle_error(self):
        return JJService._handle_error(self)


