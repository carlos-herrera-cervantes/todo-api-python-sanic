from sanic.response import json
from sanic import Blueprint
from bson.objectid import ObjectId
from json import loads

from managers import todo_manager
from repositories import todo_repository
from decorators.common_decorators import validate_role, authorize_request
from models.role import Role
from models.status_code import StatusCode
from common.common_module import try_get_authorization_token

todo_router = Blueprint('todo_router', url_prefix='/api/v1')


@todo_router.route('/todos', methods=['GET'])
@authorize_request
@validate_role([Role.ADMIN.value])
async def get_all_async(request: any) -> json:
    result = await todo_repository.get_all_async(None, request.args)
    return json({'status': True, 'data': result})


@todo_router.route('/users/me/todos', methods=['GET'])
@authorize_request
@validate_role([Role.ADMIN.value, Role.CLIENT.value])
async def get_all_me_async(request: any) -> json:
    payload = try_get_authorization_token(request.headers)
    id = payload.get('id')
    filter = {'user': ObjectId(id)}
    result = await todo_repository.get_all_async(filter, request.args)

    return json({'status': True, 'data': result})


@todo_router.route('/todos/<id>', methods=['GET'])
@authorize_request
@validate_role([Role.ADMIN.value])
async def get_by_id_async(request: any, id: str) -> json:
    result = await todo_repository.get_by_id_async(id)
    return json({'status': True, 'data': result})


@todo_router.route('/users/me/todos/<id>', methods=['GET'])
@authorize_request
@validate_role([Role.ADMIN.value, Role.CLIENT.value])
async def get_by_id_me_async(request: any, id: str) -> json:
    payload = try_get_authorization_token(request.headers)
    user_id = payload.get('id')
    filter = {'user': ObjectId(user_id), '_id': ObjectId(id)}
    result = await todo_repository.get_one_async(filter, request.args)

    return json({'status': True, 'data': result})


@todo_router.route('/todos', methods=['POST'])
@authorize_request
@validate_role([Role.ADMIN.value])
async def create_async(request: any) -> json:
    todo = request.json
    result = await todo_manager.create_async(todo)
    return json({'status': True, 'data': result}, status=StatusCode.CREATED.value)


@todo_router.route('/users/me/todos', methods=['POST'])
@authorize_request
@validate_role([Role.ADMIN.value, Role.CLIENT.value])
async def create_me_async(request: any) -> json:
    payload = try_get_authorization_token(request.headers)
    user_id = payload.get('id')
    request.json['user'] = user_id
    result = await todo_manager.create_async(request.json)

    return json({'status': True, 'data': result}, status=StatusCode.CREATED.value)


@todo_router.route('/todos/<id>', methods=['PATCH'])
@authorize_request
@validate_role([Role.ADMIN.value])
async def update_by_id_async(request: any, id: str) -> json:
    result = await todo_manager.update_by_id_async(id, request.json)
    return json({'status': True, 'data': result})


@todo_router.route('/users/me/todos/<id>', methods=['PATCH'])
@authorize_request
@validate_role([Role.ADMIN.value, Role.CLIENT.value])
async def update_by_id_me_async(request: any, id: str) -> json:
    payload = try_get_authorization_token(request.headers)
    user_id = payload.get('id')
    
    filter = {'user': ObjectId(user_id), '_id': ObjectId(id)}

    result = await todo_manager.update_one_async(filter, request.json)
    return json({'status': True, 'data': result})


@todo_router.route('/todos/<id>', methods=['DELETE'])
@authorize_request
@validate_role([Role.ADMIN.value])
async def delete_by_id_async(request: any, id: str) -> json:
    await todo_manager.delete_by_id_async(id)
    return json({'status': True, 'data': {}}, status=StatusCode.NO_CONTENT.value)


@todo_router.route('/users/me/todos/<id>', methods=['DELETE'])
@authorize_request
@validate_role([Role.ADMIN.value, Role.CLIENT.value])
async def delete_by_id_me_async(request: any, id: str) -> json:
    payload = try_get_authorization_token(request.headers)
    user_id = payload.get('id')
    
    filter = {'user': ObjectId(user_id), '_id': ObjectId(id)}

    await todo_manager.delete_one_async(filter)
    return json({'status': True, 'data': {}}, status=StatusCode.NO_CONTENT.value)