from datetime import datetime, timedelta
import logging
import jwt
from flask import request
from functools import wraps

from sql.utils import session

from .secret import SECRET
from .constants import JWT_DT_CREATED_FORMAT
from .models import User


def authenticate(fn):
    @wraps(fn)
    @session
    def wrap(*args, **kwargs):
        session = kwargs.get('session')
        if session:
            del kwargs['session']
        headers = request.headers
        token = headers.get('X-Access-Token')
        print(f'{headers}, asdf')
        if not token:
            return {'message' : 'Token is missing!!'}, 401
  
        try:
            print(token)
            data = jwt.decode(token, SECRET, algorithms=['HS256'])
            print("Hell")
            print(data)
            username = data.get('username')
            # dt_created = data.get('dt_created')
            # dt_created = datetime.strptime(JWT_DT_CREATED_FORMAT)
            # now = datetime.now()
            # time_delta = now - dt_created
            # diff_days = time_delta.days
            # if diff_days > 7:
            #     return {
            #         'message': 'Token Expired!!!'
            #     }, 401
            print(username)
            current_user = session.query(User) \
                                  .filter(User.username == username) \
                                  .first()

            kwargs['current_user'] = current_user

        except Exception as e:
            print(str(e))
            return {
                'message' : 'Token is invalid !!'
            }, 401
        return  fn(*args, **kwargs)
    return wrap