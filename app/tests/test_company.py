import pytest
from fastapi.testclient import TestClient
import sys
import os

# Adding the root directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from main import app

client = TestClient(app)

def test_crud_company():
    
    ### metadata for test ###
    metadata = dict(
        name="Test Company",
        email="test@example.com",
        password="Test12345678",
        role="supervisor"
    )
    
    ### create company ###
    response = client.post("/helpdesk/api/company", json=metadata)
    assert response.status_code == 201
    id = response.json()["id"]
    
    
    