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
        self.code = 0
        self.request = request
   
    def _parse_request(self):
        self.sns_type = request_util.get_value(self.request, para.TYPE)
        self.sns_type = str_util.get_int_value(self.sns_type)

        self.sns_id = request_util.get_value(self.request, para.SNS_ID)
        self.sns_token = request_util.get_value(self.request, para.SNS_TOKEN)
        self.sns_nick = request_util.get_value(self.request, para.SNS_NICK)
        
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
        ip = self.request.remote_addr
        user = user_manager.snslogin(self.sns_type, self.sns_id, self.sns_token, self.sns_nick, ip=ip)
#TODO set/update session
        pbuser = user.build_pb()
        return pbuser.SerializeToString()
#except:
#self.code = USER_NOT_EXISTS_ERROR
#       return JJService._handle_error(self)

