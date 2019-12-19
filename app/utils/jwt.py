# -*- coding: utf-8 -*-
"""
    Created by Space on 2019/4/25 15:25
"""

__author__ = "Space"

from flask import current_app, request
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from functools import wraps
from .error_code import AuthFailed, ParameterException
import  redis


def initRedis():
    return redis.Redis(db=current_app.config['REDIS_DB'])


def generate_auth_token(openId, channelType,
                        expiration=7200):
    """生成令牌"""
    s = Serializer(current_app.config['SECRET_KEY'],
                   expires_in=expiration)
    return s.dumps({
        'openId': openId,
        'channelType': channelType,
        'exp': expiration
    })


def jwt_auth_third(func):
    @wraps(func)
    def jwt_auth(*args, **kwargs):
        jwt = request.headers.get('Authorization')
        if jwt:
            if jwt.startswith('Bearer'):
                jwt = jwt.replace('Bearer ', '')
                s = Serializer(current_app.config['SECRET_KEY'])
                try:
                    third_user = s.loads(jwt, return_header=True)
                except:
                    raise AuthFailed(errmsg='jwt auth faild', errcode=1002)
            else:
                raise AuthFailed(errmsg='jwt auth faild', errcode=1002)
        else:
            raise AuthFailed(errmsg='jwt auth faild', errcode=1002)
        return func(third_user[0], *args, **kwargs)

    return jwt_auth



