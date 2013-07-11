# -*- coding: utf-8 -*-

"""
    Action related api
"""

from flask import Blueprint

bp = Blueprint('actions', __name__, url_prefix='/api/actions')

@bp.route('/add')
def add_action():
    return ''