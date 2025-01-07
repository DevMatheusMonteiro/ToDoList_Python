import requests

BASE_URL = "http://127.0.0.1:5000"
tasks = []

def test_create_task():
    task = {"title": "Tarefa 1", "description": "Estudar Testes Automatizados no Python", "completed": True}
    response = requests.post(f"{BASE_URL}/tasks", json=task)
    assert response.status_code == 200
    response_json = response.json()
    assert "message" in response_json
    assert "id" in response_json