from sqlalchemy import Integer, Column, String

from .database import Base
# from . import schemas, models
# from database import engine

# models.Base.metadata.create_all(bind=engine)


class Blog(Base):

    __tablename__ = 'blogs'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    body = Column(String)
