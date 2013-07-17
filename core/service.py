# -*- coding: utf-8 -*-
import common.utils.str_util
import common.utils.request_util
import logging


from flask import request
from pbmodels.response_pb2 import *
from common.utils.response_util import *

class Service(object):

    def save(self, model):
        pass

    def update(self):
        pass

    def delete(self):
        pass

    def find(self):
        pass

    def find_all(self):
        pass

class JJService(object):

    logging.basicConfig(level = logging.DEBUG)
    log = logging.getLogger('Service')

    def __init__(self, request):
        self.code = 0
        self.data = None
        self.request = request

    

    #protected methods, to be override
    def _parse_request(self):
        return True

    def _check_parameters(self):
        return True

    def _authenticate(self):
        return True

    def _handle_data(self):
        return self.__class__.__name__

    def _handle_error(self):
        response = get_error_response(self.code)
        return response.SerializeToString()

    #should not be override!!
    def handle(self):
#        try:
            self._parse_request()

            if not self._check_parameters():
                self.code = PARAMETER_ERROR 
                return self._handle_error()
            if not self._authenticate():
                self.code = AUTH_ERROR 
                return self._handle_error()
            return self._handle_data()
#        except:
#            self.code = SYSTEM_ERROR
#            response = get_error_response(self.code)
#            return response.SerializeToString()

