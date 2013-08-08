import string

def get_type_value(tp, str_value, default_value):
    try:
        return tp(str_value)
    except:
        return default_value

def get_str_value(str_value, default_value = ''):
    return get_type_value(str, str_value, default_value)

def get_int_value(str_value, default_value = 0):
    return get_type_value(int, str_value, default_value)

def get_float_value(str_value, default_value = 0.0):
    return get_type_value(float, str_value, default_value)

def is_empty(str_value):
    return not str_value or not str_value.strip()

def get_bool_value(str_value, default_value = False):
    return get_type_value(bool, str_value, default_value)

def get_list_value(str_value, split="::"):
    try:
        return str_value.split(split)
    except:
        return None
