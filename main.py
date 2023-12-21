from flask import Flask

from sql.setup import create_all

app = Flask('task_manager')

print("Hello_Main")
from sql import *
from user import *
from task_manager import *

routes = [
    # user routes
    ('/user/signup', user_signup_api, ['POST']),
    ('/user/login', login_api, ['POST']),

    # Task routes
    ('/task/create', create_task_api, ['POST']),
    ('/task/list', list_task_api, ['GET']),
    ('/task/update/<task_id>', update_task_api, ['PUT']),
    ('/task/delete/<task_id>', delete_task_api, ['DELETE'])
]

for route in routes:
    api_url = route[0]
    handler = route[1]
    methods = route[2]
    app.add_url_rule(api_url, "{}|{}".format(route, handler), handler, methods=methods)


create_all()


# @app.route('/')
# def hello_world():
#     return 'Hello, Cartoon'

app.run(host='127.0.0.1', port=8080, debug=True)