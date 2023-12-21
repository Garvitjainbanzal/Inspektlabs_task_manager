import logging
from sqlalchemy.exc import SQLAlchemyError
from sql import session
from task_manager.models import Task

@session
def create_task(taskname, user, session=None):
    if not taskname:
        return {
            'error': 'task name missing'
        }, 400

    task = Task()
    task.taskname = taskname
    task.user = user.username

    session.add(task)
    try:
        session.commit()
    except SQLAlchemyError as commit_error:
        logging.info(str(commit_error), exc_info=True)
        return {
            'error': str(commit_error)
        }

    return task.seralize(), 200

@session
def list_task(user, session=None):
    tasks = session.query(Task) \
                   .filter(Task.user == user.username) \
                   .all()

    task_list = []
    for task in tasks:
        task_list.append(task.seralize())

    return {
        'username': user.username,
        'task_list': task_list
    }, 200


@session
def delete_task(task_id, user, session=None):
    task = session.query(Task) \
                  .filter(Task.id == task_id, Task.user == user.username) \
                  .first()

    session.delete(task)
    try:
        session.commit()
    except SQLAlchemyError as commit_error:
        logging.info(str(commit_error), exc_info=True)
        return {
            'error': str(commit_error)
        }, 500

    return {
        'message': 'Deleted',
        'task_id': task_id
    }, 200


@session
def update_task(task_id, taskname, task_status, user, session=None):
    task = session.query(Task) \
                  .filter(Task.id == task_id, Task.user == user.username) \
                  .first()

    task.taskname = taskname
    task.task_status = task_status
    session.add(task)

    try:
        session.commit()
    except SQLAlchemyError as commit_error:
        logging.info(str(commit_error), exc_info=True)
        return {
            'error': str(commit_error)
        }, 500

    return {
        'message': 'Updated',
        'task': task.seralize()
    }, 200