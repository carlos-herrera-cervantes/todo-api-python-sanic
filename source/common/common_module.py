from jwt import decode

from settings import SECRET_KEY
from models.encryptor import Encryptor


def parse_pages(query_params: dict) -> dict:
    """
    :param query_params: Query parameters of request
    :return: Dictionary with page and page size attributes
    """
    if query_params.get('page', 0) == 0:
        return {'page': 0, 'page_size': 10}

    page = 0 if query_params.get('page') == '1' else int(query_params.get('page')) - 1
    page_size = int(query_params.get('page_size'))
    return {'page': page, 'page_size': page_size}


def set_paginator_object(query_params: dict, total_docs: int) -> dict:
    """
    :param query_params: Query parameters of request
    :param total_docs: Total documents of collection
    :return: Dictionary with page, page size, remaining docs and total docs attributes
    """
    page = query_params.get('page', 1)
    page_size = query_params.get('pageSize', 10)
    clone_page = 1 if page < 1 else page
    take = clone_page * page_size

    return {
        'page': clone_page,
        'pageSize': 10 if page_size < 1 else page_size,
        'remainingDocuments': 0 if (totalDocuments - take) <= 0 else totalDocuments - take,
        'totalDocs': total_docs,
    }


def try_get_authorization_token(headers: dict) -> dict:
    """
    :param headers: Headers of request
    :return: Payload that signed the token
    """
    token = headers.get('Authorization')

    try:
        payload = decode(token.split(' ').pop(), SECRET_KEY, algorithms=[Encryptor.HS256.value])
        return payload
    except Exception:
        return False
