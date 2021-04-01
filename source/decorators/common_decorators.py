from functools import wraps
from jwt import decode
from sanic.response import json

from settings import SECRET_KEY
from locales.translations import get_text
from models.status_code import StatusCode
from models.encryptor import Encryptor
from models.key_translation import KeyTranslation


def authorize_request(fn: any) -> any:
    """
    Validates token of request
    """
    @wraps(fn)
    def inner(request: any, *args: dict, **kwargs: dict) -> any:
        response = {
            'status': False,
            'code': KeyTranslation.INVALID_TOKEN.value,
            'message': get_text(request.headers, KeyTranslation.INVALID_TOKEN.value)
        }

        try:
            token = request.headers.get('Authorization')

            if token is None:
                return json(response, status=StatusCode.UNAUTHORIZED.value)

            decode(token.split(' ').pop(), SECRET_KEY, algorithms=[Encryptor.HS256.value])
            return fn(request, *args, **kwargs)
        except Exception:
            return json(response, status=StatusCode.UNAUTHORIZED.value)
    return inner


def validate_role(roles: list) -> any:
    """
    :param roles: Roles which this operation admits
    :return: Function
    """
    def wrapped(fn: any) -> any:
        @wraps(fn)
        def inner(request: any, *args: dict, **kwargs: dict) -> any:
            token = request.headers.get('Authorization')
            payload = decode(token.split(' ').pop(), SECRET_KEY, algorithms=[Encryptor.HS256.value])
            role = payload['role']

            if role not in roles:
                return json({
                    'status': False,
                    'code': KeyTranslation.INVALID_PERMISSIONS.value,
                    'message': get_text(request.headers, KeyTranslation.INVALID_PERMISSIONS.value)
                }, status=StatusCode.FORBIDDEN.value)

            return fn(request, *args, **kwargs)
        return inner
    return wrapped
