from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"

def test_readiness():
    response = client.get("/ready")
    assert response.status_code == 200
    assert response.json()["status"] == "ready"

def test_generate_demo():
    response = client.post("/generate", json={"prompt": "Explain RAG"})
    assert response.status_code == 200
    body = response.json()
    assert body["mode"] == "demo"
    assert "Explain RAG" in body["answer"]
    assert response.headers["X-Request-ID"] == body["request_id"]

def test_generate_rejects_empty_prompt():
    response = client.post("/generate", json={"prompt": ""})
    assert response.status_code == 422
