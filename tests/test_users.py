import requests
from flask import Flask

app = Flask(__name__)

# client = app.test_client()
mock_data = {'users': ['sam', 'anton', 'mike']}
mock_requests = [ {'request 1': ' hey i am requesting for a car fix'}, {'request 2 ': ' hey i amm requesting for a fix'}]


class TestUser_api:
    def test_create_user_request(self):
        """ Test api to create a user request """
        response = requests.post('/api/v1/<string:request_name>')
        assert response.status_code == 201

    def test_get_all_user_requests(self):
        """ Test api to get all the  requests created by the users """
        response = requests.get('/api/v1/requests')
        assert response.status_code == 200

    def test_get_user_request_by_id(self):
        """ Test api to get all the  requests created by the users """
        response = requests.get('/api/v1/request/<int:id>')
        assert response.status_code == 200

    def test_update_user_request_by_id(self):
        """ Test api to modify all the  request created by the user"""
        response = requests.put('/api/v1/request/<int:id>', data={'request_name': 'I am request an update'})
        assert response.status_code == 204
