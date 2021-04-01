from bson.objectid import ObjectId
from bson.json_util import dumps
from json import loads
from mongoengine import Document

from serializers.common_serializer import default
from common.common_module import parse_pages
from common.mongodb_module import build_lookup_filter


def get_all_generic(model: any, mongo_filter: dict, query_params: dict, model_name: str = '') -> list:
    """
    :param model: MongoDB collection
    :param mongo_filter: The specific document criteria
    :param query_params: Dictionary with query params of request
    :param model_name: Model name
    :return: Documents
    """
    pages = parse_pages(query_params)
    sort = loads(query_params.get('sort')) if query_params.get('sort') else {'created_at': -1}
    reference = query_params.get('with')
    query_filter = loads(query_params.get('filter')) if query_params.get('filter') else {}
    filter = mongo_filter if mongo_filter else query_filter

    pipeline = build_lookup_filter(reference, model_name)
    pipeline.append({'$sort': sort})
    pipeline.append({'$skip': pages['page']})
    pipeline.append({'$limit': pages['page_size']})
    pipeline.append({'$match': filter})

    docs = model.objects().aggregate(*pipeline)
    return loads(dumps(docs), object_hook=default)


def get_by_id_generic(model: any, id: str, query_params: dict = {}, model_name: str = '') -> Document:
    """
    :param model: MongoDB collection
    :param id: The specific document ID to retrieve
    :param query_params: Dictionary with query params of request
    :param model_name: Model name
    :return: Document
    """
    reference = query_params.get('with')

    pipeline = build_lookup_filter(reference, model_name)
    pipeline.append({'$match': {'_id': ObjectId(id)}})

    doc = model.objects().aggregate(*pipeline)
    return loads(dumps(doc), object_hook=default)


def get_one_generic(model: any, filter: dict, query_params: dict = {}, model_name: str = '') -> Document:
    """
    :param model: MongoDB collection
    :param filter: The specific document criteria to retrieve
    :param query_params: Dictionary with query params of request
    :param model_name: Model name
    :return: Document
    """
    reference = query_params.get('with')

    pipeline = build_lookup_filter(reference, model_name)
    pipeline.append({'$match': filter})

    doc = model.objects().aggregate(*pipeline)
    return loads(dumps(doc), object_hook=default)


def count_generic(model: any, filter: dict = {}) -> int:
    """
    :param model: MongoDB collection
    :param filter: The specific document criteria to count
    :return: Number of documents
    """
    return model.objects(__raw__=filter).count()
