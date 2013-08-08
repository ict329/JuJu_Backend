from core.service import JJService
import constant.para as R
import common.utils.request_util as request_util
import users.manager as user_manager
import common.utils.str_util as str_util
from users.user import *

class UpdateProfileService(JJService):
    def __init__(self, request):
        JJService.__init__(self, request)

    def _parse_request(self):
        
        atts = ('password', 'new_password', 'nick', 'role', 'gender', \
                'status', 'introduction', 'birth_date', \
                'country_code', 'province', 'city', 'tags');

        paras = (R.PASSWORD, R.NEW_PASSWORD, R.NICK, R.ROLE,\
                R.GENDER, R.STATUS, R.INTRODUCTION, R.BIRTH_DATE, \
                R.COUNTRY_CODE, R.PROVINCE, R.CITY, R.TAGS)        

        map(JJService._set_get_value_from_request, atts, paras)
        self.role = str_util.get_int_value(self.role)
        self.gender = str_util.get_bool_value(self.gender)
        self.status = str_util.get_int_value(self.status)
        self.country_code = str_util.get_int_value(self.country_code)
        self.tags = str_util.get_list_value(self.tags)

    def _check_parameters(self):
        if not JJService._check_parameters(self): 
            return False
        if str_util.is_empty(self.uid):
            return False
        return True

    def _authenticate(self):
        if not JJService._authenticate(self):
            return False
        #TODO check the password
        return True

    def _handle_data(self):
        try:
            self.avatar = request_util.get_file(self.request, para.AVATAR)
            user = user_manager.update_profile(self.uid, new_password=self.new_password, \
                        nick=self.nick, gender=self.gender, status = self.status, \
                        introduction=self.introduction, birth_date=self.birth_date, \
                        country_code=self.country_code, province=self.province, city=self.city,\
                        tags=self.tags,
                        ) 
            res = response_util.get_error_response(SUCCESS)
            user.update_pb(res.user)
            return res.SerializeToString()
        except:
            return UNKNOW_ERROR_RESPONSE.SerializeToString()

