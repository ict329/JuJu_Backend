from flask import request
from core.service import JJService
import common.utils.request_util as request_util
import common.utils.str_util as str_util 
import common.utils.response_util as response_util
import relations.manager as relation_manager

class MarkFriendService(JJService):
    def __init__(self, request):
        JJService.__init__(self, request)
   
    def _parse_request(self):
        self.fid = request_util.get_value(self.request, 'fid')
        self.mark = request_util.get_value(self.request, 'mark')
        
    def _check_parameters(self):
        if not JJService._check_parameters(self):
            return False
        if str_util.is_empty(self.uid) or str_util.is_empty(self.fid):
            return False
        return True

    def _authenticate(self):
        if not JJService._authenticate(self):
            return False
        return True

    def _handle_data(self):
        relation_manager.mark_friend(self.uid, self.fid, self.mark)    
        return response_util.SUCCESS_RESPONSE.SerializeToString()
