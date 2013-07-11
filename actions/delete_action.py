from flask import request
from core.service import JJService

class DeleteActionService(JJService):
    def __init__(self, request):
        self.code = 0
        self.data = None
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
        return self.__class__.__name__ 

    def _handle_error(self):
        return self.__class__.__name__ 
