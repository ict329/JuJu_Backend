from flask import request
from core.service import JJService
import common.utils.request_util as request_util
import common.utils.str_util as str_util 
import common.utils.response_util as response_util
import relations.manager as relation_manager
from pbmodels.response_pb2 import *

class GetBlacksService(JJService):
    def __init__(self, request):
        JJService.__init__(self, request)
   
    def _parse_request(self):
        self.uid = request_util.get_value(self.request, 'uid')

        self.offset = request_util.get_value(self.request, 'offset')
        self.offset = str_util.get_int_value(self.offset, 0)

        self.count = request_util.get_value(self.request, 'count')
        self.count = str_util.get_int_value(self.count, 20)

        
    def _check_parameters(self):
        if not JJService._check_parameters(self):
            return False
        if str_util.is_empty(self.uid):
            return False
        return True

    def _authenticate(self):
        if not JJService._authenticate(self):
            return False
        return True

    def _handle_data(self):
        users = relation_manager.get_black_list(self.uid, self.offset, self.count)
        if len(users) > 0:
            res = PBResponse()
            response_util.update_users(res, users)
            return res.SerializeToString()
        else:
            return response_util.SUCCESS_RESPONSE.SerializeToString()
