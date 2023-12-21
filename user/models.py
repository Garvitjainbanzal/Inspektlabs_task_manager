from sqlalchemy import Boolean, Column, String
from sql import Base

class User(Base):
    __tablename__ = 'user'

    username = Column(String(64), nullable=False, unique=True, primary_key=True)
    password = Column(String(108), nullable=False)
    logged_in = Column(Boolean, nullable=False, default=False)

    def __repr__(self) -> str:
        return f'{self.username}:{self.logged_in}'

    def serialize(self) -> dict:
        return {
            'username': self.username,
            'logged_id': self.logged_in
        }
