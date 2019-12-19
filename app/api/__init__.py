# -*- coding: utf-8 -*-
"""
    Created by Space on 2019/12/19 18:46
"""
__author__ = "Space"

from flask import Blueprint

api=Blueprint("api",__name__)

from app.api.v1 import token