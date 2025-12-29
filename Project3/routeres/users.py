from typing import Annotated, Optional

from fastapi import APIRouter, Depends, HTTPException
from passlib.context import CryptContext
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session
from starlette import status

from database import SessionLocal
from models import Users

from .auth import get_current_user

router = APIRouter(prefix='/user', tags=['user'])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]
user_dependency = Annotated[dict, Depends(get_current_user)]
bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


class UserVerification(BaseModel):
    password: str
    new_password: str = Field(min_length=6)


class UserResponse(BaseModel):
    id: int
    username: str
    email: str
    first_name: str
    last_name: str
    role: str
    phone_number: Optional[str] = Field(default=None)
    
    class Config:
        orm_mode = True


@router.get('/', response_model=UserResponse, status_code=status.HTTP_200_OK)
async def get_user(user: user_dependency, db: db_dependency):
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail='Authentication Failed')

    current_user = db.query(Users).filter(Users.id == user.get('id')).first()
    return current_user

    # Alternatively, if you want to return a dictionary without the hashed password: Bad practice
    # user_dict = current_user.__dict__
    # user_dict.pop('hashed_password', None)
    # return user_dict


@router.put('/password', status_code=status.HTTP_204_NO_CONTENT)
async def change_password(user: user_dependency, db: db_dependency, user_verification: UserVerification):
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail='Authentication Failed')

    current_user = db.query(Users).filter(Users.id == user.get('id')).first()
    if not bcrypt_context.verify(user_verification.password, current_user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail='Error on password change')

    current_user.hashed_password = bcrypt_context.hash(
        user_verification.new_password)
    db.add(current_user)
    db.commit()


# OR '/phone_number/{phone_number}
@router.put('/phone_number', status_code=status.HTTP_204_NO_CONTENT)
async def change_phone_number(user: user_dependency, db: db_dependency, phone_number: str):
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail='Authentication Failed')

    current_user = db.query(Users).filter(Users.id == user.get('id')).first()
    current_user.phone_number = phone_number
    db.add(current_user)
    db.commit()
