from asgiref.sync import sync_to_async

from models.todo import Todo
from .base_repository import get_all_generic, get_by_id_generic, get_one_generic, count_generic


@sync_to_async
def get_all_async(filter: dict = {}, query_params: dict = {}) -> list:
    """
    :param query_params: Dictionary with query params of request
    :param filter: The specific todo criteria
    :return: Array of ToDo
    """
    return get_all_generic(Todo, filter, query_params, 'todo')


@sync_to_async
def get_by_id_async(id: str, query_params: dict = {}) -> Todo:
    """
    :param str id: The specific todo ID to retrieve
    :param dict query_params: Dictionary with query params of request
    :return: ToDo document
    """
    return get_by_id_generic(Todo, id, query_params, 'todo')


@sync_to_async
def get_one_async(filter: dict, query_params: dict = {}) -> Todo:
    """
    :param dict filter: The specific todo criteria to retrieve
    :param dict query_params: Dictionary with query params of request
    :return: ToDo document
    """
    return get_one_generic(Todo, filter, query_params, 'todo')


@sync_to_async
def count_async(filter: dict = {}) -> int:
    """
    :param dict filter: The specific todo criteria to count
    :return: Number of to-dos
    """
    return count_generic(Todo, filter)
