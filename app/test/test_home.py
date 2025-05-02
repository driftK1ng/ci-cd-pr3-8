from app.main import app
from fastapi.testclient import TestClient
import pytest

client = TestClient(app)

def test_home():
    data = client.get("/")
    print(data.json())
    assert data.status_code == 200
    assert data.json() == "Hello docker!"