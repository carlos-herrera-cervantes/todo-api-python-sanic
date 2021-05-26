from sanic.response import json
from sanic import Blueprint
from jwt import encode
from datetime import datetime, timedelta

from settings import SECRET_KEY
from models.encryptor import Encryptor
from repositories import user_repository

auth_router = Blueprint('auth_router', url_prefix='/api/v1')


@auth_router.route('/auth/login', methods=['POST'])
async def login(request: dict) -> json:
    email = request.json.get('email', '')
    pipeline_result = await user_repository.get_one_async({'email': email})
    user = pipeline_result.pop()

    token = encode({
        'id': str(user['id']),
        'email': email,
        'role': user['role'],
        'exp': datetime.utcnow() + timedelta(days=7)
    }, SECRET_KEY, algorithm=Encryptor.HS256.value)

    return json({'status': True, 'data': token.decode('ascii')})
