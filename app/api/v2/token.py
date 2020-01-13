# -*- coding: utf-8 -*-
"""
    Created by Space on 2020/1/13 15:23
"""
__author__ = "Space"

from app.api.v2 import api
from app.api import api_success_result


@api.route('/test')
def test():
    return api_success_result("hello world ")
