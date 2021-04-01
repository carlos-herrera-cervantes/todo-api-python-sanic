from enum import Enum


class StatusCode(Enum):
    UNAUTHORIZED = 401
    FORBIDDEN = 403
    BAD_REQUEST = 400
    NOT_FOUND = 404
    INTERNAL_SERVER_ERROR = 500
    OK = 200
    CREATED = 201
    NO_CONTENT = 204
