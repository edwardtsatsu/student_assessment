# Import necessary modules
import json
import pytest
from flask import Flask
from src.controllers.auth_controller import auth_bp

@pytest.fixture
def app():
    app = Flask(__name__)
    app.register_blueprint(auth_bp)
    return app

@pytest.fixture
def client(app):
    return app.test_client()

def test_login_endpoint(client):
    response = client.post('/login', json={'username': 'test_user', 'password': 'test_password'})

    assert response.status_code == 200

    response_data = json.loads(response.data)
    assert 'message' not in response_data

def test_student_login_endpoint(client):
    response = client.post('/student/login', json={'username': 'test_student', 'password': 'test_password'})

    assert response.status_code == 200

    response_data = json.loads(response.data)
    assert 'message' not in response_data 
