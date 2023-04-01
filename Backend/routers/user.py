from datetime import timedelta
from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, status
from sqlalchemy.orm import Session
from Backend.auth.auth import ACCESS_TOKEN_EXPIRE_MINUTES, authenticate_user, create_access_token, Token, get_password_hash, get_current_user

from Backend.dependencies import get_db

from ..database import crud, models, schemas
from ..database.database import SessionLocal, engine

from fastapi.security import OAuth2PasswordRequestForm

models.Base.metadata.create_all(bind=engine)


user_router = FastAPI()


@user_router.post("/user", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_username(db, username=user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="username already registered")
    user.password = get_password_hash(user.password)
    return crud.create_user(db=db, user=user)


@user_router.get("/user/me", response_model=schemas.User)
def get_user(
    current_user: Annotated[schemas.User, Depends(get_current_user)]
):
    return current_user


@user_router.post("/token", response_model=Token)
def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: Session = Depends(get_db)):
    user = authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}