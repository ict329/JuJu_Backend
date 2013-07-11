# -*- coding: utf-8 -*-

"""
    Relation related api
"""
from flask import Blueprint


bp = Blueprint('relations', __name__, url_prefix='/api/relations')

@bp.route('/get')
def get_relation():
    pass