from flask import request

from user.auth_middleware import authenticate

from .utils import create_task, list_task, update_task, delete_task

@authenticate
def create_task_api(current_user):
    req = request.get_json(silent=True)
    if not req:
        return {
            'error': 'Cannot json parse request body'
        }, 400

    taskname = req.get('taskname')

    return create_task(taskname, current_user)


@authenticate
def list_task_api(current_user):
    return list_task(current_user)


@authenticate
def update_task_api(task_id, current_user):
    req = request.get_json(silent=True)
    if not req:
        return {
            'error': 'Cannot json parse request body'
        }, 400

    taskname = req.get('taskname')
    task_status = req.get('task_name')

    return update_task(task_id, taskname, task_status, current_user)


@authenticate
def delete_task_api(task_id, current_user):
    return delete_task(task_id, current_user)