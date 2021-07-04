import json

import pytest

from backend.task.models import Task


@pytest.mark.usefixtures("db")
class TestTaskAPI:
    def test_list_task(self, client):
        data_list = [
            {"id": 1, "name": "test1", "status": 0},
            {"id": 2, "name": "test2", "status": 0},
            {"id": 3, "name": "test3", "status": 0},
            {"id": 4, "name": "test4", "status": 0},
        ]
        for data in data_list:
            Task(name=data["name"]).save()

        response = client.get("/tasks")
        assert response.status_code == 200
        assert response.headers["Content-Type"] == "application/json"
        assert json.loads(response.data) == { "result": data_list}

    def test_create_task(self, client):
        new_test_data = {
            "id": 1,
            "name": "new_test",
            "status": 0,
        }
        response = client.post("/task", json={
            "name": new_test_data["name"],
        })
        assert response.status_code == 201
        assert response.headers["Content-Type"] == "application/json"
        assert json.loads(response.data) == { "result": new_test_data}

    def test_create_task_validate_error(self, client):
        new_test_data = {
            "id": 1,
            "name": "t" * 101,
            "status": 0,
        }
        response = client.post("/task", json={
            "name": new_test_data["name"],
        })
        assert response.status_code == 400
        assert response.headers["Content-Type"] == "application/json"
        assert json.loads(response.data) == {"name": ["Length must be between 1 and 100."]}

    def test_update_task(self, client):
        Task(name="update_me").save()

        updated_test_data = {
            "id": 1,
            "name": "updated_test",
            "status": 1,
        }
        response = client.put(f"/task/{updated_test_data['id']}", json={
            "id": updated_test_data["id"],
            "name": updated_test_data["name"],
            "status": updated_test_data["status"],
        })
        assert response.status_code == 200
        assert response.headers["Content-Type"] == "application/json"
        assert json.loads(response.data) == updated_test_data

    def test_update_task_id_not_exist(self, client):
        Task(name="update_me").save()

        updated_test_data = {
            "id": 2,
            "name": "updated_test",
            "status": 1,
        }
        response = client.put(f"/task/{updated_test_data['id']}", json={
            "id": updated_test_data["id"],
            "name": updated_test_data["name"],
            "status": updated_test_data["status"],
        })
        assert response.status_code == 400
        assert response.headers["Content-Type"] == "application/json"
        assert json.loads(response.data) == {"id": ["not exist"]}

    def test_update_task_id_not_match(self, client):
        Task(name="update_me").save()

        updated_test_data = {
            "id": 1,
            "name": "updated_test",
            "status": 1,
        }
        response = client.put(f"/task/{updated_test_data['id'] + 1}", json={
            "id": updated_test_data["id"],
            "name": updated_test_data["name"],
            "status": updated_test_data["status"],
        })
        assert response.status_code == 400
        assert response.headers["Content-Type"] == "application/json"
        assert json.loads(response.data) == {"id": ["not match"]}

    def test_update_task_validate_error(self, client):
        Task(name="update_me").save()

        updated_test_data = {
            "id": 1,
            "name": "t" * 101,
            "status": 2,
        }
        response = client.put(f"/task/{updated_test_data['id']}", json={
            "id": updated_test_data["id"],
            "name": updated_test_data["name"],
            "status": updated_test_data["status"],
        })
        assert response.status_code == 400
        assert response.headers["Content-Type"] == "application/json"
        assert json.loads(response.data) == {"status": ["Must be greater than or equal to 0 and less than or equal to 1."], "name": ["Length must be between 1 and 100."]}

    def test_delete_task(self, client):
        task = Task(name="delete_me").save()
        response = client.delete(f"/task/{task.id}")
        assert response.status_code == 200
        assert response.headers["Content-Type"] == "application/json"

    def test_delete_task_id_not_exist(self, client):
        task = Task(name="delete_me").save()
        response = client.delete(f"/task/{task.id + 1}")
        assert response.status_code == 400
        assert response.headers["Content-Type"] == "application/json"
        assert json.loads(response.data) == {"id": ["not exist"]}