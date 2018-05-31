import pytest
import requests


@pytest.fixture()
def client(request):
    def teardown():
        pass

    request.addfinalizer(teardown)


def test_get_all_user_requests():
    """ Test api to get all the  requests created by the users """
    response = requests.get('https://maintainencetrackerapi.herokuapp.com/api/v1/user/requests')
    assert response.status_code, 200
    assert response.headers['content-type'] == 'application/json'
    assert b'request' in response.content
    assert b'id' in response.content


def test_auth_user_request_without_authentication():
    """ if check if i can get user requests without logging in
     this should fail """
    response1 = requests.get('https://maintainencetrackerapi.herokuapp.com/api/v1/user/requests')
    assert response1.status_code, 401
    assert response1.headers['content-type'] == 'application/json'
