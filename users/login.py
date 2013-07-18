import constant.para as para
import common.utils.request_util as request_util
import common.utils.str_util as str_util 
import users.manager as user_manager

from flask import request
from core.service import JJService
from users.user import User
from pbmodels.response_pb2 import *


class LoginService(JJService):
    def __init__(self, request):
        self.code = 0
        self.request = request
   
    def _parse_request(self):
        self.uname = request_util.get_value(self.request, para.UNAME)
        self.password = request_util.get_value(self.request, para.PASSWORD)
        self.latitude = request_util.get_value(self.request, para.LATITUDE)
        self.latitude = str_util.get_float_value(self.latitude)
        self.longitude = request_util.get_value(self.request, para.LONGITUDE)
        self.longitude = str_util.get_float_value(self.longitude)
        self.ip = self.request.remote_addr
        
    def _check_parameters(self):
        if not JJService._check_parameters(self):
            return False
        return True

    def _authenticate(self):
        if not JJService._authenticate(self):
            return False
        return True

    def _handle_data(self):
        try:
            user = user_manager.login(self.uname, self.password, ip=self.ip, latitude=self.latitude, longitude=self.longitude)
#TODO set/update session
            pbuser = user.build_pb()
            return pbuser.SerializeToString()
        except:
            self.code = USER_NOT_EXISTS_ERROR
            return JJService._handle_error(self)
