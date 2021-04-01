from asgiref.sync import sync_to_async

from models.user import User
from .base_repository import get_all_generic, get_by_id_generic, get_one_generic, count_generic


@sync_to_async
def get_all_async(filter: dict = {}, query_params: dict = {}) -> list:
    """
    :param query_params: Dictionary with query params of request
    :param filter: The specific user criteria
    :return: List of users
    """
    return get_all_generic(User, filter, query_params, 'user')


@sync_to_async
def get_by_id_async(id: str, query_params: dict = {}) -> User:
    """
    :param id: The specific user ID to retrieve
    :param query_params: Dictionary with query params of request
    :return: User
    """
    return get_by_id_generic(User, id, query_params, 'user')


@sync_to_async
def get_one_async(filter: dict, query_params: dict = {}) -> User:
    """
    :param filter: The specific user criteria to retrieve
    :param query_params: Dictionary with query params of request
    :return: User
    """
    return get_one_generic(User, filter, query_params, 'user')


@sync_to_async
def count_async(filter: dict = {}) -> int:
    """
    :param dict filter: The specific user criteria to count
    :return: Number of users
    """
    return count_generic(User, filter)
