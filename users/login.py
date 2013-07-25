import constant.para as para
import common.utils.request_util as request_util
import common.utils.str_util as str_util 
import users.manager as user_manager

from flask import request
from core.service import JJService
from users.user import User
from pbmodels.response_pb2 import *
from common.utils.response_util import *


class LoginService(JJService):
    def __init__(self, request):
        JJService.__init__(self, request)
   
    def _parse_request(self):
        self.uname = request_util.get_value(self.request, para.UNAME)
        self.password = request_util.get_value(self.request, para.PASSWORD)


        self.latitude = request_util.get_value(self.request, para.LATITUDE)
        self.latitude = str_util.get_float_value(self.latitude)
        self.longitude = request_util.get_value(self.request, para.LONGITUDE)
        self.longitude = str_util.get_float_value(self.longitude)
        self.ip = self.request.remote_addr

        self.device_id = request_util.get_value(self.request, para.DEVICE_ID)
        self.device_os = request_util.get_value(self.request, para.DEVICE_OS)
        self.device_name = request_util.get_value(self.request, para.DEVICE_NAME)
        self.device_token = request_util.get_value(self.request, para.DEVICE_TOKEN)
        
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
            user = user_manager.login(self.uname, self.password, \
                    ip=self.ip, latitude=self.latitude, longitude=self.longitude, \
                    device_id=self.device_id, device_name=self.device_name, \
                    device_os=self.device_os, device_token=self.device_token)

            self.session['uid'] = str(user.pk)
            self.session['uname']
            self.session['role'] = user.basic_info.role
            res = SUCCESS_RESPONSE
            user.update_pb(res.user)
            return res.SerializeToString()
        except:
            self.code = USER_NOT_EXISTS_ERROR
            return JJService._handle_error(self)
