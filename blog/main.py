from fastapi import FastAPI, Depends, Response, HTTPException

from fastapi import FastAPI, Depends, Response, HTTPException
from sqlalchemy.orm import Session
from starlette import status

from blog import models
from blog.database import engine, get_db
from blog.hashing import Hash
from blog.schemas import Blog, ShowBlog, User, ShowUser
from routers import blog

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(blog.router)


# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()


@app.post('/blogschema', status_code=status.HTTP_201_CREATED, tags=['blog'])
def create_blog(request: Blog, db: Session = Depends(get_db)):
    new_blog = models.Blog(title=request.title, body=request.body, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


# @app.get('/blogall', response_model=List[ShowBlog], tags=['blog'])
# def get_all_blog(db: Session = Depends(get_db)):
#     blogs = db.query(models.Blog).all()
#     return blogs


@app.get('/blog/{id}', status_code=200, response_model=ShowBlog, tags=['blog'])
def get_blog_by_id(id: int, response: Response, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with this {id} is not found")
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {'error_response': f'Blog with this {id} not found'}
    return blog


@app.delete('/blog/{id}', status_code=status.HTTP_204_NO_CONTENT, tags=['blog'])
def destroy(id, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with this {id} is not found")
    else:
        blog.delete(synchronize_session=False)
        db.commit()
        return 'done'


@app.put('/blog/{id}', status_code=status.HTTP_202_ACCEPTED, tags=['blog'])
def update(id, request: Blog, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with this {id} is not found")

    else:
        blog.update({'title': request.title, 'body': request.body})
        db.commit()
        return 'updated'


@app.post('/createuser', status_code=status.HTTP_201_CREATED, response_model=ShowUser, tags=['user'])
def create_user(request: User, db: Session = Depends(get_db)):
    hashed_password = Hash().bcrypt(request.password)
    new_user = models.User(name=request.name, email=request.email, password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@app.get("/getuser/{id}", status_code=status.HTTP_200_OK, response_model=ShowUser, tags=['user'])
def getuser(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {id} is not found")
    else:
        return user
