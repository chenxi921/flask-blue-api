# -*- coding: utf-8 -*-
"""
    Created by Space on 2020/1/13 15:23
"""
__author__ = "Space"

from flask import Blueprint

api = Blueprint("v2", __name__)
from app.api.v2 import token