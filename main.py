from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def index():
    return {'data': {'name': 'Anu'}}


@app.get('/about')
def about():
    return {'data': {'page_name': 'About Page'}}
