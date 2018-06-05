import unittest

import app


class AppTestCase(unittest.TestCase):
    def setUp(self):
        print("==> starting up the env tests")
        app.app.config['TESTING'] = True
        self.app = app.app.test_client()
        self.dummy_data = {'id': 10, 'request': 'I am requesting a car fix',
                           "status": True, "request_type": "repair", "request_details": "This the description"}

    def tearDown(self):
        print("==>Tearing down after tests!")

    def test_get_user_request(self):
        """Test user can create a request"""
        resp = self.app.get('/api/v1/user/request/3')
        self.assertEqual(resp.status_code, 200)
        self.assertIn(b'request', resp.data)

    def test_api_all_user_request(self):
        resp = self.app.get('/api/v1/user/requests')
        assert resp.status_code, 200
        assert resp.headers['content-type'] == 'application/json'
        assert b'request' in resp.data
        assert b'id' in resp.data

    def test_api_create_request(self):
        resp = self.app.post('/api/v1/user/request/10', json={'id': 4, "request": "iam requesting", "status": True,
                                                              "request_type": "repair",
                                                              "request_details": "This the description"})
        self.assertEqual(resp.status_code, 201)

    def test_api_update_request(self):
        resp = self.app.put('/api/v1/user/request/10', json={'id': 4, "request": "iam requesting", "status": True,
                                                             "request_type": "repair",
                                                             "request_details": "This is updated"})
        self.assertEqual(resp.status_code, 200)

    def test_api_delete_request(self):
        resp = self.app.delete('/api/v1/user/request/1')
        self.assertEqual(resp.status_code, 202)
        self.assertNotIn(b'id', resp.data)
        self.assertIn(b'Message', resp.data)
        # assert resp.status_code, 202

#
# import pytest
# import requests
#
#
# @pytest.fixture()
# def client(request):
#     def teardown():
#         pass
#
#     request.addfinalizer(teardown)
#
#
# def test_get_all_user_requests():
#     """ Test api to get all the  requests created by the users """
#     response = requests.get('https://maintainencetrackerapi.herokuapp.com/api/v1/user/requests')
#     assert response.status_code, 200
#     assert response.headers['content-type'] == 'application/json'
#     assert b'request' in response.content
#     assert b'id' in response.content
#
#
# def test_auth_user_request_without_authentication():
#     """ if check if i can get user requests without logging in
#      this should fail """
#     response1 = requests.get('https://maintainencetrackerapi.herokuapp.com/api/v1/user/requests')
#     assert response1.status_code, 401
#     assert response1.headers['content-type'] == 'application/json'
