from fastapi import FastAPI

print("🟢 RUNNING THE CORRECT main.py FILE")

app = FastAPI()

@app.get('/')
def index():
    return {'data': {'name': 'Anu'}}

@app.get('/about')
def about():
    return {'data': {'page_name': 'About Page'}}

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
def comments(blog_id: int,comment_id:int):
    print("COMMENTS ROUTE HIT")
    return {'blog_id': blog_id,'comment_id':comment_id}

@app.get('/simpledata')
def get_simple_data():
    return {'data': {'arrays':{'1','2'}}}
