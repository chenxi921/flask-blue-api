# -*- coding: utf-8 -*-
"""
    Created by Space on 2019/12/19 18:46
"""
__author__ = "Space"

from flask import jsonify



def api_success_result(data):
    result = {
        'errcode': 0,
        'data': data,
        'errmsg': ""
    }
    return jsonify(result), 201