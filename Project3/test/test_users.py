from routeres.users import get_db, get_current_user
from .utils import *
from fastapi import status

app.dependency_overrides[get_db] = override_get_db
app.dependency_overrides[get_current_user] = override_get_current_user


def test_return_user(test_user):
    response = client.get('/user')
    assert response.status_code == status.HTTP_200_OK
    print(response.json())
    assert response.json() == {'id': 1, 'username': 'mmahamed', 'email': 'mmahamed@gmail.com', 'first_name': 'Mojtaba',
                               'last_name': 'Mahamed', 'role': 'admin', 'phone_number': '09127575757'}


def test_change_password_success(test_user):
    response = client.put(
        '/user/password', json={'password': '123456', 'new_password': 'testpassword'})
    assert response.status_code == status.HTTP_204_NO_CONTENT


def test_change_password_invalid_current_password(test_user):
    response = client.put(
        '/user/password', json={'password': 'wrong_password', 'new_password': 'testpassword'})
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    assert response.json() == {'detail': 'Error on password change'}


def test_change_phone_number_success(test_user):
    response = client.put('/user/phone_number',
                          params={'phone_number': '09121112121'})
    assert response.status_code == status.HTTP_204_NO_CONTENT
