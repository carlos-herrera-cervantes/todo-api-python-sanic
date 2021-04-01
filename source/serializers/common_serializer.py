from datetime import datetime
from mongoengine import Document


def default(document: Document) -> Document:
    """
    :param document: MongoDB document
    :return: Document
    """
    if '_id' in document.keys():
        document['id'] = document['_id']['$oid']

    if 'created_at' in document.keys():
        document['created_at'] = datetime.fromtimestamp(document['created_at']['$date'] / 1000).isoformat()
        document['updated_at'] = datetime.fromtimestamp(document['updated_at']['$date'] / 1000).isoformat()

    document.pop('_id', None)
    document.pop('password', None)

    return document
