import app

def test_health():
    client = app.app.test_client()
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json["status"] == "ok"


def test_info():
    client = app.app.test_client()
    response = client.get("/info")
    assert response.status_code == 200
    assert "app" in response.json


def test_home():
    client = app.app.test_client()
    response = client.get("/")
    assert response.status_code == 200