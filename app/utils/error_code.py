# -*- coding: utf-8 -*-
from app.utils.error import APIException


class Success(APIException):
    code = 201
    errmsg = 'ok'
    errcode = 0


class DeleteSuccess(Success):
    code = 202
    errcode = 1


class ServerError(APIException):
    code = 500
    errmsg = 'unknown exception'
    errcode = 999


class ClientTypeError(APIException):
    # 400 401 403 404
    # 500
    # 200 201 204
    # 301 302
    code = 400
    errmsg = 'client is invalid'
    errcode = 1006


class ParameterException(APIException):
    code = 400
    errmsg = 'invalid parameter'
    errcode = 1000


class NotFound(APIException):
    code = 404
    errmsg = 'the resource are not found O__O...'
    errcode = 1001


class AuthFailed(APIException):
    code = 401
    errcode = 1005
    errmsg = 'authorization failed'


class Forbidden(APIException):
    code = 403
    errcode = 1004
    errmsg = 'forbidden, not in scope'


class DuplicateGift(APIException):
    code = 400
    errcode = 2001
    errmsg = 'the current book has already in gift'
