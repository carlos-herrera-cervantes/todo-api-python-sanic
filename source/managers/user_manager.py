from asgiref.sync import sync_to_async

from models.user import User
from .base_manager import create_generic, update_by_id_generic, delete_by_id_generic


@sync_to_async
def create_async(user: User) -> User:
    """
    :param user: User object model
    :return: User
    """
    return create_generic(User, user)


@sync_to_async
def update_by_id_async(id: str, user: User) -> User:
    """
    :param id: User ID to update
    :param user: User object model
    :return: User
    """
    return update_by_id_generic(User, id, user)


@sync_to_async
def delete_by_id_async(id: str) -> None:
    """
    :param id: User ID to delete
    :return: Deleted count
    """
    return delete_by_id_generic(User, id)
