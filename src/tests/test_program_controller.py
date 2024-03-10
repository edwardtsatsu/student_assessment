# Import necessary modules
import json
import pytest
from flask import Flask
from src.controllers.program_controller import program_bp

@pytest.fixture
def app():
    app = Flask(__name__)
    app.register_blueprint(program_bp)
    return app

@pytest.fixture
def client(app):
    return app.test_client()

def test_index_endpoint(client):
    response = client.get('/')

    assert response.status_code == 200

    assert isinstance(response.json, list)

def test_store_endpoint(client):
    response = client.post('/', json={'name': 'New Program', 'description': 'Program description'})

    assert response.status_code == 201

    assert 'name' in response.json

def test_update_endpoint(client):
    response = client.put('/some_program_id', json={'name': 'Updated Program', 'description': 'Updated description'})

    assert response.status_code == 200

    assert 'name' in response.json 

def test_destroy_endpoint(client):
    response = client.delete('/some_program_id')

    assert response.status_code == 204

    assert not response.data
