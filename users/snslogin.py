from flask import request
from core.service import JJService
import constant.para as para
import common.utils.request_util as request_util
import common.utils.str_util as str_util
import users.manager as user_manager
from users.user import User
from pbmodels.response_pb2 import *


class SNSLoginService(JJService):
    def __init__(self, request):
        JJService.__init__(self, request)
   
    def _parse_request(self):
        self.sns_type = request_util.get_value(self.request, para.TYPE)
        self.sns_type = str_util.get_int_value(self.sns_type)

        self.sns_id = request_util.get_value(self.request, para.SNS_ID)
        self.sns_token = request_util.get_value(self.request, para.SNS_TOKEN)
        self.sns_nick = request_util.get_value(self.request, para.SNS_NICK)
        
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
#        try:
        user = user_manager.snslogin(self.sns_type, self.sns_id, self.sns_token, self.sns_nick,  \
                ip=self.ip, latitude=self.latitude, longitude=self.longitude, \
                device_id=self.device_id, device_name=self.device_name, \
                device_os=self.device_os, device_token=self.device_token)
#TODO set/update session
        pbuser = user.build_pb()
        return pbuser.SerializeToString()
#except:
#self.code = USER_NOT_EXISTS_ERROR
#       return JJService._handle_error(self)

