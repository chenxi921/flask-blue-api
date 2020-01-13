# -*- coding: utf-8 -*-
"""
    Created by Space on 2019/12/19 18:44
"""

from flask import Flask
from app.utils.limiter import Limiter
from flask_cors import *
from app.model.base import db
import argparse

parser = argparse.ArgumentParser(description='manual to this script')
parser.add_argument('--env', type=str, default=None)
args = parser.parse_args()

limiter = Limiter()


def create_app():
    if args:
        env = args.env
    else:
        env = "dev"
    app = Flask(__name__)
    CORS(app, supports_credentials=True)
    app.config.from_object("app.config.%s.secure" % env)
    app.config.from_object("app.config.%s.setting" % env)
    register_blueprint(app)
    db.init_app(app)
    return app


def register_blueprint(app):
    from app.api.v1 import api
    from app.api.v2 import api as api_v2
    app.register_blueprint(api, url_prefix="/api")
    app.register_blueprint(api_v2, url_prefix="/api2")
