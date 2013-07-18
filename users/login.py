from flask import request
from core.service import JJService
import constant.para as para
import common.utils.request_util as request_util
import users.user_manager as user_manager
from users.user import User
from pbmodels.response_pb2 import *


class LoginService(JJService):
    def __init__(self, request):
        self.code = 0
        self.request = request
   
    def _parse_request(self):
        self.uname = request_util.get_value(self.request, para.UNAME)
        self.password = request_util.get_value(self.request, para.PASSWORD)
        
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
            user = user_manager.login(self.uname, self.password)
#TODO set/update session
            pbuser = user.build_pb()
            return pbuser.SerializeToString()
        except:
            self.code = USER_NOT_EXISTS_ERROR
            return JJService._handle_error(self)
