from flask import request
from core.service import JJService
import constant.para as para
import common.utils.request_util as request_util
import common.utils.response_util as response_util


class LogoutService(JJService):
    def __init__(self, request):
        self.code = 0
        self.request = request
   
    def _parse_request(self):
        pass

    def _check_parameters(self):
        if not JJService._check_parameters(self):
            return False
        return True

    def _authenticate(self):
        if not JJService._authenticate(self):
            return False
        return True

    def _handle_data(self):
        return response_util.SUCCESS_RESPONSE.SerializeToString() 
#TODO delete user session
