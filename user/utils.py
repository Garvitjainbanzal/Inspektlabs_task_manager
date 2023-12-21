import logging
import jwt
from datetime import datetime
from sqlalchemy.exc import SQLAlchemyError

from sql.utils import session
from user.constants import JWT_DT_CREATED_FORMAT

from .models import User
from .secret import SECRET

@session
def create_user(username, password, session=None):
    user = User(username=username, password=password)
    #user.useprname = username
    #user.password = password

    session.add(user)
    try:
        session.commit()
    except SQLAlchemyError as commit_error:
        logging.info(str(commit_error), exc_info=True)

    return user.serialize()


@session
def login(username, password, session=None):
    user = session.query(User) \
                  .filter(User.username == username) \
                  .first()

    logging.info(user)

    if user.password != password:
        return {}

    token = generate_token(username)

    return {
        'message': 'Login Successful',
        'auth_token': token
    }


def generate_token(username):
    payload = {
        'username': username,
        'dt_created': datetime.now().strftime(JWT_DT_CREATED_FORMAT)
    }

    token = jwt.encode(payload, SECRET)

    return token
