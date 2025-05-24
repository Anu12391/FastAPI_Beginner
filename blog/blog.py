from fastapi import FastAPI

app = FastAPI()


@app.post('/blogschema')
def create_blog():
    return 'creating'
