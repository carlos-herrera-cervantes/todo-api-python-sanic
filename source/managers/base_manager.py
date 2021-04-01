from json import loads
from bson.objectid import ObjectId
from mongoengine import Document

from serializers.common_serializer import default


def create_generic(model: any, document: Document) -> Document:
    """
    :param model: MongoDB collection
    :param document: MongoDB document
    :return: Document
    """
    created = model(**document).save().to_json()
    return loads(created, object_hook=default)


def update_by_id_generic(model: any, id: str, document: Document) -> Document:
    """
    :param model: MongoDB collection
    :param id: The document ID to update
    :param document: MongoDB document
    :return: Document
    """
    model.objects(id=ObjectId(id)).update_one(**document)
    updated = model.objects.get(id=ObjectId(id))
    updated.save()
    return loads(updated.to_json(), object_hook=default)


def update_one_generic(model: any, filter: dict, document: Document) -> Document:
    """
    :param model: MongoDB collection
    :param filter: Filter to apply
    :param document: Document dictionary
    :return: Document
    """
    model.objects(__raw__=filter).update_one(**document)
    updated = model.objects.get(__raw__=filter)
    updated.save()
    return loads(updated.to_json(), object_hook=default)


def delete_by_id_generic(model: any, id: str) -> None:
    """
    :param model: MongoDB collection
    :param id: Document ID to delete
    :return: Deleted count
    """
    return model.objects(id=ObjectId(id)).delete()


def delete_one_generic(model: any, filter: dict) -> None:
    """
    :param model: MongoDB collection
    :param filter: Filter to apply
    :return: True if success otherwise throw an error
    """
    return model.objects(__raw__=filter).delete()


def delete_many_generic(model: any, filter: dict) -> None:
    """
    :param model: MongoDB collection
    :param filter: Filter to apply on removal
    :return: Removed count
    """
    return model.objects(__raw__=filter).delete()
