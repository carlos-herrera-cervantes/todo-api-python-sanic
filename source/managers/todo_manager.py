from asgiref.sync import sync_to_async

from models.todo import Todo
from .base_manager import ( 
    create_generic,
    update_by_id_generic,
    update_one_generic,
    delete_by_id_generic,
    delete_many_generic,
    delete_one_generic
)


@sync_to_async
def create_async(todo: Todo) -> Todo:
    """
    :param todo: Todo object model
    :return: Todo
    """
    return create_generic(Todo, todo)


@sync_to_async
def update_by_id_async(id: str, todo: Todo) -> Todo:
    """
    :param id: The ToDo ID to update
    :param todo: Todo object model
    :return: Todo
    """
    return update_by_id_generic(Todo, id, todo)


@sync_to_async
def update_one_async(filter: dict, todo: Todo) -> Todo:
    """
    :param filter: Filter to apply
    :param todo: Todo object model
    :return: Todo
    """
    return update_one_generic(Todo, filter, todo)


@sync_to_async
def delete_by_id_async(id: str) -> None:
    """
    :param id: The ToDo ID to delete
    :return: Deleted count
    """
    return delete_by_id_generic(Todo, id)


@sync_to_async
def delete_one_async(filter: dict) -> None:
    """
    :param filter: Filter to apply
    :return: Deleted count
    """
    return delete_one_generic(Todo, filter)


@sync_to_async
def delete_many_async(filter: dict) -> None:
    """
    :param filter: Filter to apply on removal
    :return: Removed count
    """
    return delete_many_generic(Todo, filter)
