from datetime import timedelta

from fastapi import APIRouter, HTTPException
from fastapi.params import Depends
from sqlalchemy.orm import Session
from starlette import status

from blog import database, models
from blog.database import get_db
from blog.hashing import Hash
from blog.schemas import Login, Token
from routers.token import create_access_token, ACCESS_TOKEN_EXPIRE_MINUTES

router = APIRouter(tags=["Authentication"], prefix="/user")


@router.post('/login')
def login(request: Login, db: Session = Depends(get_db)):
    hashObj:Hash=Hash()
    user = db.query(models.User).filter(models.User.email == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Invalid Credentials")
    if not hashObj.verify(user.password, request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Invalid Password")
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.email}
    )

    return Token(access_token=access_token, token_type="bearer")
