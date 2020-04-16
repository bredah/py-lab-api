import requests
import json

base_url = "https://jsonplaceholder.typicode.com"


def test_get():
    # Make the request
    response = requests.get(base_url + "/todos/1")
    # Validate the response status code
    assert response.status_code == 200
    # Validate the response JSON values
    response_value = json.loads(response.text)
    assert response_value["userId"] == 1
    assert response_value["id"] == 1
    assert response_value["title"] == "delectus aut autem"
    assert not response_value["completed"]


def test_post():
    # Request body
    body = {
        'title': "foo",
        'body': "bar",
        'userId': 1
    }
    # Request header
    headers = {
        "Content-type": "application/json; charset=UTF-8"
    }
    # Make the request
    response = requests.post(base_url + "/posts", headers=headers, data=json.dumps(body))
    # Validate the response JSON values
    response_value = json.loads(response.text)
    # Validate the response status code
    assert response.status_code == 201
    # Validate the response JSON values
    response_value = json.loads(response.text)
    assert response_value['title'] == body['title']
    assert response_value['body'] == body['body']
    assert response_value['userId'] == body['userId']
    assert response_value["id"] == 101


def test_put():
    # Request body
    body = {
        'id': 1,
        'title': "foo",
        'body': "bar",
        'userId': 1
    }
    # Request header
    headers = {
        "Content-type": "application/json; charset=UTF-8"
    }
    # Make the request
    response = requests.put(base_url + "/posts/1", headers=headers, data=json.dumps(body))
    # Validate the response JSON values
    response_value = json.loads(response.text)
    # Validate the response status code
    assert response.status_code == 200
    # Validate the response JSON values
    response_value = json.loads(response.text)
    assert response_value['title'] == body['title']
    assert response_value['body'] == body['body']
    assert response_value['userId'] == body['userId']
    assert response_value['id'] == body['id']


def test_delete():
    # Make the request
    response = requests.delete(base_url + "/posts/1")
    # Validate the response status code
    assert response.status_code == 200
