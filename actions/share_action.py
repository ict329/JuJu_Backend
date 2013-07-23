from flask import request
from core.service import JJService

class ShareActionService(JJService):
    def __init__(self, request):
        JJService.__init__(self, request)
   
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
        return self.__class__.__name__ 

    def _handle_error(self):
        return self.__class__.__name__ 
