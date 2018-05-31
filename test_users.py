import unittest

import requests


# client = app.test_client()
# mock_data = {'users': ['sam', 'anton', 'mike']}

class ApiTest(unittest.TestCase):
    """ This represents the api test class for doing tdd """

    def setUp(self):
        """ Intialize all the variables to be used in testing the app"""

        self.mock_data = {'request_name': 'phone_repair'}

    def test_create_user_request(self):
        """ Test api to create a user request """
        response = requests.post('/api/v1/<string:request_name>', data=self.mock_data)
        self.assertEqual(response.status_code, 201)
        self.assertIn('phone_repair', str(response.text))

    def test_get_all_user_requests(self):
        """ Test api to get all the  requests created by the users """
        response = requests.post('/api/v1/requests', data=self.mock_data)
        self.assertEqual(response.status_code, 201)
        response = requests.get('/api/v1/requests', )
        self.assertEqual(response.status_code, 200)
        self.assertIn('phone_repair', str(response.text))

    def test_get_user_request_by_id(self):
        """ Test api to get all the  requests created by the users """
        response = requests.post('/api/v1/request/<int:id>', data=self.mock_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('phone_repair', str(response.text))

    def test_update_user_request_by_id(self):
        """ Test api to modify all the  request created by the user"""
        response = requests.post('/api/v1/request/<int:id>', data={'request_name': 'I need a bug fix'})
        self.assertEqual(response.status_code, 201)
        update_request = requests.post('/api/v1/request/<int:id>', data={'request_name': 'Fix me'})
        self.assertEqual(update_request.status_code, 202)
        result = requests.get('/api/v1/request/<int:id>')
        self.assertIn('Fix me', str(result.text))
