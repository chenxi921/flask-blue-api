# -*- coding: utf-8 -*-
"""
    Created by Space on 2019/12/19 18:46
"""

__author__ = "Space"

from app.api import api
from app.api.v1 import api_success_result


@api.route('/test')
def test():
    return api_success_result("welcome %")
