from flask import request
from core.service import JJService
import users.manager as user_manager
import common.utils.response_util as response_util
from users.user import *

class GetProfileService(JJService):
    def __init__(self, request):
        JJService.__init__(self, request)
   
    def _parse_request(self):
        pass 
        
    def _check_parameters(self):
        if not JJService._check_parameters(self):
            return False
        if not self.uid:
            return False
        return True

    def _authenticate(self):
        if not JJService._authenticate(self):
            return False
        return True

    def _handle_data(self):
        user = user_manager.get_user(self.uid)
        if user:
            res = response_util.get_error_response(SUCCESS)
            #TODO cut some attributes from user
            user.update_pb(res.user)
            return res.SerializeToString() 
        return UNKNOW_ERROR_RESPONSE.SerializeToString()
