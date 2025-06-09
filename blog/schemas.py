from __future__ import annotations

from typing import List
from pydantic import BaseModel




class User(BaseModel):
    name: str
    email: str
    password: str



class ShowUser(BaseModel):
    name: str
    email: str
    blogs: List[Blog] = []



    class Config:
        orm_mode = True


class ShowBlog(BaseModel):
    title: str
    body: str
    creator: ShowUser

    class Config:
        orm_mode = True


class BlogBase(BaseModel):
    title: str
    body: str


class Blog(BlogBase):
    title: str
    body: str
    class Config:
        orm_mode = True



