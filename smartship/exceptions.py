# -*- coding: utf-8 -*-


class ApiError(Exception):
    def __init__(self, message, code, response):
        super(ApiError, self).__init__(message)
        self.code = code
        self.response = response
