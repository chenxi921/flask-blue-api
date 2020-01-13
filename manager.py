# -*- coding: utf-8 -*-
"""
    Created by Space on 2019/4/23 16:44
"""
__author__ = "Space"

from app import create_app
from app.utils.error import APIException
from app.utils.error_code import ServerError
from werkzeug.exceptions import HTTPException

app = create_app()


@app.errorhandler(Exception)
def framework_error(e):
    if isinstance(e, APIException):
        return e
    if isinstance(e, HTTPException):
        code = e.code
        msg = e.description
        error_code = 1007
        return APIException(msg, code, error_code)
    else:
        # 调试模式
        # log
        if not app.config['DEBUG']:
            return ServerError()
        else:
            raise e


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=app.config["DEBUG"], port=8888)
