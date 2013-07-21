# -*- coding: utf-8 -*-
# -*- 2013-07-16 -*-

def update_pb_with_document(pbmodel, document, fields):
    for field in fields:
        if field != None and  hasattr(document, field) and hasattr(pbmodel, field):
            value = getattr(document, field)
            if value is not None:
                setattr(pbmodel, field, value)


def update_pb_with_list(pbmodel, field, lst):
    if field is not None and lst is not None:
        if hasattr(pbmodel, field):
            value = getattr(pbmodel, field)
            if value is not None:
                value.extend(lst)
        
    
def update_pb_with_value(pbmodel, field, value):
    if field is not None and value is not None:
        if hasattr(pbmodel, field):
            setattr(pbmodel, field, value)
    
