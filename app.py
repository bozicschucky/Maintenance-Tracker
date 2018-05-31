from flask import Flask
from flask_jwt import JWT, jwt_required
from flask_restful import Resource, Api
from security import authenticate, identity

app = Flask(__name__)
app.secret_key = 'Code'
api = Api(app)

jwt = JWT(app, authenticate, identity)

requests = [
    {'id': 1, 'request': 'I am requesting a car fix'},
    {'id': 2, 'request': 'This is the second request'}
]


class UserRequest(Resource):
    @jwt_required()
    def get(self, id):
        for item in requests:
            if item['id'] == id:
                return item
        # item = next(filter(lambda x:x['name'] == name,items), None)
        return {'Request': None}, 404



class UserRequests(Resource):
    @jwt_required()
    def get(self):
        return {'requests': requests}

api.add_resource(UserRequest, '/api/v1/user/request/<int:id>')
api.add_resource(UserRequests, '/api/v1/user/requests')

if __name__ == '__main__':
    app.run(debug=True)
