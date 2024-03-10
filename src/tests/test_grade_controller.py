# Import necessary modules
import json
import pytest
from flask import Flask
from src.controllers.grade_controller import grade_bp

@pytest.fixture
def app():
    app = Flask(__name__)
    app.register_blueprint(grade_bp)
    return app

@pytest.fixture
def client(app):
    return app.test_client()

def test_index_endpoint(client):
    response = client.get('/')

    assert response.status_code == 200

    assert isinstance(response.json, list)

def test_store_endpoint(client):
    response = client.post('/', json={'grade': 'A', 'min_score': 90, 'max_score': 100})

    assert response.status_code == 201

    assert 'grade' in response.json

def test_update_endpoint(client):
    response = client.put('/some_grade_id', json={'grade': 'A+', 'min_score': 95, 'max_score': 100})

    assert response.status_code == 200

    assert 'grade' in response.json

def test_destroy_endpoint(client):
    response = client.delete('/some_grade_id')

    assert response.status_code == 204

    assert not response.data
