# -*- coding: utf-8 -*-
from enum import IntEnum


class ResponseCode(IntEnum):
    OK = 200
    CREATED = 201
    MISSING = 400
    UNAUTHORIZED = 401
    VALIDATION_ERROR = 422
    SERVER_ERROR = 500
