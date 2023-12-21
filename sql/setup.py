from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine('mysql+mysqlconnector://root:password@localhost:3306/task_manager')
Session = sessionmaker(bind=engine)

Base = declarative_base()


def create_all():
    Base.metadata.create_all(engine, checkfirst=True)