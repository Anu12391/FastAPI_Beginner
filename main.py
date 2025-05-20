from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

print("🟢 RUNNING THE CORRECT main.py FILE")

app = FastAPI()


@app.get('/')
def index():
    return {'data': {'name': 'Anu'}}


@app.get('/about')
def about():
    return {'data': {'page_name': 'About Page'}}


@app.get('/blog/unpublished')
def unpublished():
    return {'data': 'unpublished'}


@app.get('/blog/{blog_id}')
def show(blog_id: int):
    return {'data': blog_id}


@app.get('/blog/{blog_id}/comments')
def comments(blog_id: int):
    print("COMMENTS ROUTE HIT")
    return {'data': blog_id}


@app.get('/justtest')
def mytest():
    return {'data': 'hii'}


@app.get('/blog/{blog_id}/comments/{comment_id}')
def comments(blog_id: int, comment_id: int):
    print("COMMENTS ROUTE HIT")
    return {'blog_id': blog_id, 'comment_id': comment_id}


@app.get('/simpledata')
def get_simple_data():
    return {'data': {'arrays': {'1', '2'}}}


@app.get('/queryblog')
def query_blog_with_limit(published: bool, limit=20, sort: Optional[str] = None):
    if published:
        return {'data': f'{limit} published blogs per api call'}
    else:
        return {'data': f'{limit} blogs per api call'}


@app.post('/blogpost')
def create_blog_post():
    return {'data': 'Blog is created'}


class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]


@app.post('/blogcreate')
def create_blog_pydantic(request: Blog):
    return {'data': 'Blog is created'}
