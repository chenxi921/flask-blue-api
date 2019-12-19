# -*- coding: utf-8 -*-
from flask import request, json
from werkzeug.exceptions import HTTPException



class APIException(HTTPException):
    code = 500
    errmsg = 'sorry, we made a mistake (*￣︶￣)!'
    errcode = 999

    def __init__(self, errmsg=None, code=None, errcode=None,
                 headers=None):
        if code:
            self.code = code
        if errcode:
            self.errcode = errcode
        if errmsg:
            self.errmsg = errmsg
        super(APIException, self).__init__(errmsg, None)

    def get_body(self, environ=None):
        body = dict(
            errmsg=self.errmsg,
            errcode=self.errcode,
            data=None
            #request=request.method + ' ' + self.get_url_no_param()
        )
        text = json.dumps(body)
        return text

    def get_headers(self, environ=None):
        """Get a list of headers."""
        return [('Content-Type', 'application/json')]

    @staticmethod
    def get_url_no_param():
        full_path = str(request.full_path)
        main_path = full_path.split('?')
        return main_path[0]

