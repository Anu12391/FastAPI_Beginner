from sqlalchemy import Integer, Column, String

from database import BASE
from . import schemas, models
from database import engine

models.Base.metadata.create_all(bind=engine)


class Blog(BASE):
    id = Column(Integer, primary_key=True)
    title = Column(String)
    body = Column(String)
