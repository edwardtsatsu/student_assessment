# Import necessary modules
import json
import pytest
from flask import Flask
from src.controllers.student_controller import student_bp

@pytest.fixture
def app():
    app = Flask(__name__)
    app.register_blueprint(student_bp)
    return app

@pytest.fixture
def client(app):
    return app.test_client()

def test_index_endpoint(client):
    response = client.get('/')

    print(f"===={response.status_code}=====")

    assert response.status_code == 200

    assert isinstance(response.json, list)

def test_store_endpoint(client):
    response = client.post('/', json={'first_name': 'John', 'last_name': 'Doe', 'gender': 'male', 'date_of_birth': '1990-01-01'})

    assert response.status_code == 201

    assert 'id' in response.json

def test_update_endpoint(client):
    response = client.put('/some_student_id', json={'first_name': 'Jane'})

    assert response.status_code == 200

    assert 'first_name' in response.json

def test_destroy_endpoint(client):
    response = client.delete('/some_student_id')

    assert response.status_code == 204

    assert not response.data
