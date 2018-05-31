from auth import authenticate, identity
from flask import Flask, request
from flask_jwt import JWT, jwt_required
from flask_restful import Resource, Api

app = Flask(__name__)
app.secret_key = 'Code'
api = Api(app)

jwt = JWT(app, authenticate, identity)

requests = [
    {'id': 1, 'request': 'I am requesting a car fix',
     "status": True, "request_type": "repair", "request_details": "This the description"},
    {'id': 2, 'request': 'This is the second request',
     "status": False, "request_type": "repair", "request_details": "This the description"},
    {'id': 3, 'request': 'This is the third request',
     "status": False, "request_type": "repair", "request_details": "This the description"}
]


class UserRequest(Resource):
    @jwt_required()
    def get(self, id):
        for item in requests:
            if item['id'] == id:
                return item
        # item = next(filter(lambda x:x['name'] == name,items), None)
        return {'Request': None}, 404

    @jwt_required()
    def post(self, id):
        for item in requests:
            if item['id'] == id:
                return {'message': 'An item with {} already exits'.format(id)}, 400
        data = request.get_json()
        item = {'id': id, 'request': data['request'], 'status': data['status']
            , "request_type": data["request_type"], "request_details": data["request_details"]}
        requests.append(item)
        return item, 201

    @jwt_required()
    def put(self, id):
        data = request.get_json()
        item = next(filter(lambda x: x['id'] == id, requests), None)
        if item is None:
            item = {'id': id, 'request': data['request'], 'status': data['status']
                , "request_type": data["request_type"], "request_details": data["request_details"]}
            requests.append(item)
            requests.append(item)
        else:
            item.update(data)
        return item


class UserRequests(Resource):
    # @jwt_required()
    def get(self):
        return {'requests': requests}


api.add_resource(UserRequest, '/api/v1/user/request/<int:id>')
api.add_resource(UserRequests, '/api/v1/user/requests')

if __name__ == '__main__':
    app.run(debug=True)
