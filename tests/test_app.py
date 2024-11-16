import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app

@pytest.fixture
def client():
    # Create a test client for the Flask app
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_homepage(client):
    # Test the homepage response
    response = client.get("/")
    assert response.status_code == 200
    assert b"Welcome to My Flask App" in response.data

def test_api_data(client):
    # Test the /api/data endpoint
    response = client.get("/api/data")
    assert response.status_code == 200
    assert response.json == {"message": "Hello, World!", "status": "success"}
