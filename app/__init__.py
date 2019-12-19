# -*- coding: utf-8 -*-
"""
    Created by Space on 2019/12/19 18:44
"""

from flask import Flask
from app.utils.limiter import Limiter
from flask_cors import *
from app.model.base import db

limiter = Limiter()


def create_app():
    app = Flask(__name__)
    CORS(app, supports_credentials=True)
    app.config.from_object("app.config.secure")
    app.config.from_object("app.config.setting")
    register_blueprint(app)
    db.init_app(app)
    return app


def register_blueprint(app):
    from app.api import api
    app.register_blueprint(api)