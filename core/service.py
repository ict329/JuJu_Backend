# -*- coding: utf-8 -*-
import common.utils.str_util
import logging


from flask import request, session
from pbmodels.response_pb2 import *
from common.utils.response_util import *
from settings import *
import common.utils.request_util as request_util

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

    log = logging.getLogger('Service')

    def __init__(self, request):
        self.code = 0
        self.data = None
        self.request = request
        self.session = session
        if USE_SESSION:
            try:
                self.uid = self.session['uid']
            except:
                self.uid = None
        else:
            self.uid = request_util.get_value(request, 'uid')
            

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



# Utils 

    def _set_get_value_from_request(self, attr_name, para_name):
        try:
            value = request_util.get_value(self.request, para_name)
            setattr(self, attr_name, value)
            return value
        except:
            return None

    def _set_flie_value_from_request(self, attr_name, file_name):
        try:
            value = request_util.get_file(self.request, file_name)
            setattr(self, attr_name, value)
            return value
        except:
            return None


