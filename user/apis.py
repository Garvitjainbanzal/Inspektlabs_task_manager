from flask import request

from .utils import create_user, login

print("Hello")

def user_signup_api():
    req = request.get_json(silent=True)
    if not req:
        return {
            'error': 'Cannot json parse request body'
        }, 400

    username = req.get('username')
    password = req.get('password')

    if not (username and password):
        return {
            'error': 'Username or Password missing'
        }, 400


    return create_user(username, password), 202


def login_api():
    req = request.get_json(silent=True)

    if not req:
        return {
            'error': 'Cannot json parse request body'
        }, 400

    username = req.get('username')
    password = req.get('password')

    if not (username and password):
        return {
            'error': 'Username or Password missing'
        }, 400

    res = login(username, password)

    if not res.get('auth_token'):
        return {
            'error': 'Unauthorized access'
        }, 403

    return res, 200