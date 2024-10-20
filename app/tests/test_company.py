import pytest
from fastapi.testclient import TestClient
import sys
import os

# Adding the root directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from main import app

client = TestClient(app)

def test_crud_user():
    
    ### create user ###
    metadata = dict(
        name="Test User",
        email="test@example.com",
        password="Test12345678",
        role="supervisor",
        supervisor_id= ""
        
    )
    response = client.post("/helpdesk/api/user", json=metadata)
    assert response.status_code == 201
    id = response.json()["id"]
    
    ### read user ###
    response = client.get(f"/helpdesk/api/user/{int(id)}")
    assert response.status_code == 200
    
    ### update user ###
    metadata_put = dict(
        name="Test Update",
        email="test_update@example.com",
        password="Test12345678",
        role="supervisor",
        supervisor_id= ""
    )
    response = client.put(f"/helpdesk/api/user/{int(id)}" ,json=metadata_put)
    assert response.status_code == 200
    
    ### delete user ###
    response = client.delete(f"/helpdesk/api/user/{int(id)}")
    assert response.status_code == 200