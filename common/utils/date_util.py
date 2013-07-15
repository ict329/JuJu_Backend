# -*- coding: utf-8 -*-
# -*- 2013-07-15 -*-
import datetime, time 

def datetime_to_timestamp(dt):
    if dt is None:
        return None
    return time.mktime(dt).timetuple()) 


