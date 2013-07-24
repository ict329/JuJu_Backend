# -*- coding: utf-8 -*-
# -*- 2013-07-16 -*-

def update_pb_with_document(pbmodel, document, fields):
    for field in fields:
        if field and  hasattr(document, field) and hasattr(pbmodel, field):
            value = getattr(document, field)
            if value:
                setattr(pbmodel, field, value)


def update_pb_with_list(pbmodel, field, lst):
    if field and lst:
        if hasattr(pbmodel, field):
            value = getattr(pbmodel, field)
            if value:
                value.extend(lst)
        
    
def update_pb_with_value(pbmodel, field, value):
    if field and value:
        if hasattr(pbmodel, field):
            setattr(pbmodel, field, value)
