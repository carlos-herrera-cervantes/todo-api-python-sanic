from sanic.response import json
from sanic import Blueprint

from managers import user_manager
from repositories import user_repository
from decorators.common_decorators import validate_role, authorize_request
from models.role import Role
from models.status_code import StatusCode
from common.common_module import try_get_authorization_token

user_router = Blueprint('user_router', url_prefix='/api/v1')


@user_router.route('/users', methods=['GET'])
@authorize_request
@validate_role([Role.ADMIN.value])
async def get_all_async(request: any) -> json:
    result = await user_repository.get_all_async(None, request.args)
    return json({'status': True, 'data': result})


@user_router.route('/users/<id>', methods=['GET'])
@authorize_request
@validate_role([Role.ADMIN.value])
async def get_by_id_async(request: any, id: str) -> json:
    result = await user_repository.get_by_id_async(id)
    return json({'status': True, 'data': result})


@user_router.route('/users/me', methods=['GET'])
@authorize_request
@validate_role([Role.ADMIN.value, Role.CLIENT.value])
async def get_me_async(request: any) -> json:
    payload = try_get_authorization_token(request.headers)
    id = payload.get('id')
    me = await user_repository.get_by_id_async(id)
    return json({'status': True, 'data': me})


@user_router.route('/users', methods=['POST'])
async def create_async(request: any) -> json:
    result = await user_manager.create_async(request.json)
    return json({'status': True, 'data': result}, status=StatusCode.CREATED.value)


@user_router.route('/users/<id>', methods=['PATCH'])
@authorize_request
@validate_role([Role.ADMIN.value])
async def update_by_id_async(request: any, id: str) -> json:
    result = await user_manager.update_by_id_async(id, request.json)
    return json({'status': True, 'data': result})


@user_router.route('/users/me', methods=['PATCH'])
@authorize_request
@validate_role([Role.ADMIN.value, Role.CLIENT.value])
async def update_me_async(request: any) -> json:
    payload = try_get_authorization_token(request.headers)
    id = payload.get('id')
    result = await user_manager.update_by_id_async(id, request.json)
    return json({'status': True, 'data': result})


@user_router.route('/users/<id>', methods=['DELETE'])
@authorize_request
@validate_role([Role.ADMIN.value])
async def delete_by_id_async(request: any, id: str) -> json:
    await user_manager.delete_by_id_async(id)
    return json({'status': True, 'data': {}}, status=StatusCode.NO_CONTENT.value)