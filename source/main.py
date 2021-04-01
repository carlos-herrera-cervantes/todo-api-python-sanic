from sanic import Sanic
from sanic.response import json

from routes.user_routes import user_router
from routes.todo_routes import todo_router
from routes.authorization_routes import auth_router
from models.config import Config

Config.start_connection()
app = Sanic('TodoServer')

app.blueprint(auth_router)
app.blueprint(user_router)
app.blueprint(todo_router)


@app.route('/')
async def check_health(request: any) -> json:
    return json({'status': True, 'message': 'Server is up'})

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=3000, debug=True)
