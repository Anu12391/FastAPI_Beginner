from sqlalchemy import Integer, Column, String

from database import BASE


class Blog(BASE):
    id = Column(Integer, primary_key=True)
    title = Column(String)
    body = Column(String)
