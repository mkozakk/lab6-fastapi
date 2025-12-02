from fastapi.testclient import TestClient
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from main import app

def test_hello():
    client = TestClient(app)
    resp = client.get('/hello')
    assert resp.status_code == 200
    assert resp.json() == {"message": "Hello world"}
