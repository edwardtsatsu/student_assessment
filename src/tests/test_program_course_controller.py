# Import necessary modules
import json
import pytest
from flask import Flask
from src.controllers.program_course_controller import program_course_bp 

@pytest.fixture
def app():
    app = Flask(__name__)
    app.register_blueprint(program_course_bp)
    return app

@pytest.fixture
def client(app):
    return app.test_client()

def test_index_endpoint(client):
    response = client.get('/')

    assert response.status_code == 200

    assert isinstance(response.json, list)

def test_store_endpoint(client):
    response = client.post('/', json={'program_id': 'some_program_id', 'course_ids': ['course_id1', 'course_id2']})

    assert response.status_code == 201

    assert 'message' in response.json

