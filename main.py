from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def index():
    return {'data': {'name': 'Anu'}}


@app.get('/about')
def about():
    return {'data': {'page_name': 'About Page'}}

@app.get('/blog/{blog_id}')
def show(blog_id):
    return {'data': blog_id}
