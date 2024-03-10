# Import necessary modules
import json
import pytest
from flask import Flask
from src.controllers.semester_controller import semester_bp

@pytest.fixture
def app():
    app = Flask(__name__)
    app.register_blueprint(semester_bp)
    return app

@pytest.fixture
def client(app):
    return app.test_client()

def test_index_endpoint(client):
    response = client.get('/')

    assert response.status_code == 200

    assert isinstance(response.json, list)

def test_store_endpoint(client):
    response = client.post('/', json={'name': 'Spring 2022', 'academic_year': '2022'})

    assert response.status_code == 201

    assert 'name' in response.json

def test_update_endpoint(client):
    response = client.put('/some_semester_id', json={'name': 'Fall 2021', 'academic_year': '2021'})

    assert response.status_code == 200

    assert 'name' in response.json

def test_destroy_endpoint(client):
    response = client.delete('/some_semester_id')

    assert response.status_code == 204

    assert not response.data
