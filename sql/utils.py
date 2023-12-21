from functools import wraps
import logging

from sqlalchemy.exc import SQLAlchemyError

from .setup import Session


def session(fn):
    @wraps(fn)
    def wrap(*args, **kwargs):
        session = Session()
        kwargs['session'] = session

        try:
            result = fn(*args, **kwargs)
        except Exception as e:
            logging.error(str(e), exc_info=True)
            session.rollback()
            raise e
        finally:
            session.close()

        return result
    return wrap
