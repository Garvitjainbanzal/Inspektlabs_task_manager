from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sql import Base


class Task(Base):
    __tablename__ = 'task'

    id = Column(Integer, autoincrement=True, primary_key=True)
    user = Column(String(64), ForeignKey('user.username'), nullable=False)
    taskname = Column(String(100))
    task_status = Column(Boolean, default=False)

    def __repr__(self) -> str:
        return f'{self.taskname}:{self.task_status}'

    def seralize(self) -> dict:
        return {
            'id': self.id,
            'taskname': self.taskname,
            'task_status': self.task_status
        }