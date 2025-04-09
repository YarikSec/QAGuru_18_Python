import requests
import json

from jsonschema import validate

from schemas import *

BASE_URL = "https://reqres.in/api"

def test_get_user():
    response = requests.get(url=f"{BASE_URL}/users?page=2")
    assert response.status_code == 200

def test_create_user():
    response = requests.post(url=f"{BASE_URL}/users", data={'name': 'morpheus', 'job': 'leader'})
    assert response.status_code == 201

def test_update_user():
    response = requests.put(url=f'{BASE_URL}/users/2', data={'name': 'morpheus', 'job': 'zion resident'})
    assert response.status_code == 200

def test_delete_user():
    response = requests.delete(url=f'{BASE_URL}/users/2')
    assert response.status_code == 204

# def test_get_user_negative():
#     response = requests.get(
#         url=f"{BASE_URL}/users",
#         params={'page': ''}
#     )
#     assert response.status_code == 404

def test_unsuccessful_login():
    response = requests.post(url=f"{BASE_URL}/login", data={'email': 'peter@klaven'})
    assert response.status_code == 400
    assert json.loads(response.text) == {'error': 'Missing password'}
    assert 'Missing password' in response.text
    assert response.json()['error'] == 'Missing password'
    assert response.headers['Content-Type'] == 'application/json; charset=utf-8'

def test_create_user_schema1():
    response = requests.post(url=f"{BASE_URL}/users", data={'name': 'morpheus', 'job': 'leader'})
    body = response.json()

    assert response.status_code == 201
    with open('post_users.json') as file:
        schema = json.load(file)
        validate(instance=body, schema=schema)


def test_create_user_schema2():
    response = requests.post(url=f"{BASE_URL}/users", data={'name': 'morpheus', 'job': 'leader'})
    body = response.json()

    assert response.status_code == 201
    validate(instance=body, schema=post_users)

def test_get_single_user_schema3():
    response = requests.get(url=f"{BASE_URL}/users/2")
    body = response.json()

    assert response.status_code == 200
    validate(instance=body, schema=get_single_user)

def test_get_user_business_logic():
    response = requests.get(
        url=f'{BASE_URL}/users',
        params={"page": "2"},
        verify=False
    )

    assert response.json()['data'][0]['email'] == 'michael.lawson@reqres.in'
    assert response.json()['data'][1]['email'] == 'lindsay.ferguson@reqres.in'

def test_get_unique_users_business_logic2():
    response = requests.get(
        url=f'{BASE_URL}/users',
        params={"page": "2"},
        verify=False
    )

    ids = [element['id'] for element in response.json()['data']]

    assert len(ids) == len(set(ids))