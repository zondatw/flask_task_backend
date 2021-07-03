import json
from http import HTTPStatus

from flask import Blueprint, current_app, Response
from flask.globals import request
from marshmallow import ValidationError

from .models import Task
from .serializers import TaskListSerializer, TaskDetailSerializer

blueprint = Blueprint("task", __name__)

@blueprint.route("/tasks", methods=["GET"])
def list_tasks():
    """list_tasks

    Response all task

    example:
        response status code 200
        {
            "result": [
                {"id": 1, "name": "name", "status": 0}
            ]
        }
    """
    serializer = TaskListSerializer()
    tasks = Task.query.all()
    response_data = {
        "result": serializer.dump(tasks, many=True)
    }
    current_app.logger.info(f"List tasks response: {response_data}")
    return Response(json.dumps(response_data), status=HTTPStatus.OK, mimetype="application/json")

@blueprint.route("/task", methods=["POST"])
def create_task():
    """create task

    Create task by name, and status default value is False

    example:
        request
        {
            "name": "買晚餐"
        }

        response status code 201
        {
            "result": {"name": "買晚餐", "status": 0, "id": 1}
        }
    """
    current_app.logger.info(f"Create task request data: {request.json}")
    serializer = TaskListSerializer()
    try:
        data = serializer.load(request.json)
    except ValidationError as err:
        current_app.logger.error(f"Create task error: {err}")
        return Response(str(err), status=HTTPStatus.BAD_REQUEST, mimetype="application/json")

    task = Task.create(name=data["name"])
    response_data = {
        "result": serializer.dump(task)
    }
    current_app.logger.info(f"Create task response: {response_data}")
    return Response(json.dumps(response_data), status=HTTPStatus.CREATED, mimetype="application/json")


@blueprint.route("/task/", methods=["PUT"])
def update_task():
    """Update task

    Update task's name and status by id

    example:
        request
        {
            "name": "買早餐",
            "status": 1
            "id": 1
        }

        response status code 200
        {
            "name": "買早餐",
            "status": 1,
            "id": 1
        }
    """
    current_app.logger.info(f"update task request data: {request.json}")
    serializer = TaskDetailSerializer()
    try:
        data = serializer.load(request.json)
    except ValidationError as err:
        current_app.logger.error(f"update task error: {err}")
        return Response(str(err), status=HTTPStatus.BAD_REQUEST, mimetype="application/json")

    task = Task.query.get(data["id"])
    if not task:
        return Response(json.dumps({"id": ["not exist"]}), status=HTTPStatus.BAD_REQUEST, mimetype="application/json")
    if "name" in data:
        task.name = data["name"]
    if "status" in data:
        task.status = data["status"]
    task.save()
    
    response_data = serializer.dump(task)
    current_app.logger.info(f"update task response: {response_data}")
    return Response(json.dumps(response_data), status=HTTPStatus.OK, mimetype="application/json")


@blueprint.route("/task/", methods=["DELETE"])
def delete_task():
    """Delete task

    Delete task by id

    example:
        request
        {
            "id": 1
        }

        response status code 200
    """
    current_app.logger.info(f"delete task request data: {request.json}")
    serializer = TaskDetailSerializer()
    try:
        data = serializer.load(request.json)
    except ValidationError as err:
        current_app.logger.error(f"delete task error: {err}")
        return Response(str(err), status=HTTPStatus.BAD_REQUEST, mimetype="application/json")
    
    task = Task.query.get(data["id"])
    if not task:
        return Response(json.dumps({"id": ["not exist"]}), status=HTTPStatus.BAD_REQUEST, mimetype="application/json")
    task.delete()
    
    return Response("", status=HTTPStatus.OK, mimetype="application/json")
