from flask import request

def get_value(request, key):

    if request.args.has_key(key):
        return request.args.get(key)
    return None
