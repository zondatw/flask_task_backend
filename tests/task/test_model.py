import pytest
import sqlalchemy

from backend.task.models import Task


@pytest.mark.usefixtures("db")
class TestTaskModel:
    def test_create_task(self):
        task_name = "test"
        Task(name=task_name).save()
        task = Task.query.get(1)
        assert task.id == 1
        assert task.name == task_name
        assert task.status == 0

    def test_create_task_validate_error(self):
        task_name = "t" * 101

        with pytest.raises(sqlalchemy.exc.DataError) as err:
            Task(name=task_name).save()
        assert "Data too long for column \\\'name\\\' at row 1" in str(err)

    def test_update_task(self):
        # Create task
        task_name = "test"
        Task(name=task_name).save()
        task = Task.query.get(1)
        assert task.id == 1
        assert task.name == task_name
        assert task.status == 0

        # Update task
        updated_name = "updated_test"
        status = 1
        task = Task.query.get(1)
        task.name = updated_name
        task.status = status
        task.save()
        assert task.id == 1
        assert task.name == updated_name
        assert task.status == status

    def test_update_task_validate_error(self):
        # Create task
        task_name = "test"
        Task(name=task_name).save()
        task = Task.query.get(1)
        assert task.id == 1
        assert task.name == task_name
        assert task.status == 0

        # Update task
        updated_name = "updated_test"
        status = 2
        task = Task.query.get(1)
        task.name = updated_name
        task.status = status

        with pytest.raises(sqlalchemy.exc.StatementError) as err:
            task.save()
        assert "Value 2 is not None, True, or False" in str(err)

    def test_delete_task(self):
        # Create task
        task_name = "test"
        Task(name=task_name).save()
        task = Task.query.get(1)
        assert task.id == 1
        assert task.name == task_name
        assert task.status == 0

        # Delete task
        task = Task.query.get(1)
        task.delete()
        task = Task.query.get(1)
        assert task == None