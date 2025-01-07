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
    tasks.append(response_json["id"])

def test_get_tasks():
    response = requests.get(f"{BASE_URL}/tasks")
    assert response.status_code == 200
    assert "tasks" in response.json()
    assert "total_tasks" in response.json()

def test_get_task():
    if tasks:
        task_id = tasks[0]
        response = requests.get(f"{BASE_URL}/tasks/{task_id}")
        assert response.status_code == 200
        assert task_id == response.json()["id"]

def test_update_task():
    if tasks:
        task_id = tasks[0]
        task = {"title": "Tarefa 1", "description": "Mudando descrição pelo teste update", "completed": True}
        response = requests.put(f"{BASE_URL}/tasks/{task_id}", json=task)
        assert response.status_code == 200
        response_json = response.json()

        response = requests.get(f"{BASE_URL}/tasks/{task_id}")
        assert response.status_code == 200
        for key in task.keys():
            assert response.json()[key] == task[key]

def test_delete_task():
    if tasks:
        task_id = tasks[0]
        response = requests.delete(f"{BASE_URL}/tasks/{task_id}")
        assert response.status_code == 200

        response = requests.get(f"{BASE_URL}/tasks/{task_id}")
        assert response.status_code == 404
        