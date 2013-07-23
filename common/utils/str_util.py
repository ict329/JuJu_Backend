import string

def get_type_value(tp, str_value, default_value):
    try:
        value = tp(str_value)
        return value
    except:
        return default_value

def get_str_value(str_value, default_value = ''):
    return get_type_value(str, str_value, default_value)

def get_int_value(str_value, default_value = 0):
    return get_type_value(int, str_value, default_value)

def get_float_value(str_value, default_value = 0.0):
    return get_type_value(float, str_value, default_value)

def is_empty(str_value):
    return str_value == None or len(str_value.strip()) == 0 



