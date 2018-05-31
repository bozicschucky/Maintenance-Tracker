from flask import Flask
from flask_restful import Api

app = Flask(__name__)
app.secret_key = 'Code'
api = Api(app)

api.add_resource(UserRequest, '/api/v1/user/request/<int:id>')
api.add_resource(UserRequests, '/api/v1/user/requests')

if __name__ == '__main__':
    app.run(debug=True)
