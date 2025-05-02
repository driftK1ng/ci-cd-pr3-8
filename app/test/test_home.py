import pytest
import requests

url = "http://127.0.0.1:8000"

def test_home():
    path = "/"
    request_url = url + path
    data = requests.get(request_url)
    assert data.status_code == 200
    assert data.content == b'"Hello docker!"'