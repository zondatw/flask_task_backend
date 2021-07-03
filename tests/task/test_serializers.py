import pytest

from marshmallow import ValidationError

from backend.task.serializers import TaskListSerializer, TaskDetailSerializer
from backend.task.models import Task

class TestTaskListSerializer:
    def setup_class(self):
        self.serializer = TaskListSerializer()

    def test_validate(self):
        # status not in range 0~1
        with pytest.raises(ValidationError):
            self.serializer.load({
                "id": 1,
                "name": "test",
                "status": 2
            })

        # name max length is 100 
        with pytest.raises(ValidationError):
            self.serializer.load({
                "id": 1,
                "name": "t" * 101,
                "status": 1
            })

        # name min length is 1 
        with pytest.raises(ValidationError):
            self.serializer.load({
                "id": 1,
                "name": "",
                "status": 1
            })

    def test_dump(self):
        task = Task(id=1, name="test", status=True)
        data = self.serializer.dump(task)
        assert data == {
            "id": 1,
            "name": "test",
            "status": 1
        }

    def test_load(self):
        data = self.serializer.load({
            "id": 1,
            "name": "test",
            "status": 1
        })
        assert data == {
            "id": 1,
            "name": "test",
            "status": 1
        }

class TestTaskDetailSerializer:
    def setup_class(self):
        self.serializer = TaskDetailSerializer()

    def test_validate(self):
        # status not in range 0~1
        with pytest.raises(ValidationError):
            self.serializer.load({
                "id": 1,
                "name": "test",
                "status": 2
            })

        # name max length is 100 
        with pytest.raises(ValidationError):
            self.serializer.load({
                "id": 1,
                "name": "t" * 101,
                "status": 1
            })

        # name min length is 1 
        with pytest.raises(ValidationError):
            self.serializer.load({
                "id": 1,
                "name": "",
                "status": 1
            })

        # id is required
        with pytest.raises(ValidationError):
            self.serializer.load({
                "name": "test",
                "status": 1
            })

    def test_dump(self):
        task = Task(id=1, name="test", status=True)
        data = self.serializer.dump(task)
        assert data == {
            "id": 1,
            "name": "test",
            "status": 1
        }

    def test_load(self):
        data = self.serializer.load({
            "id": 1,
            "name": "test",
            "status": 1
        })
        assert data == {
            "id": 1,
            "name": "test",
            "status": 1
        }