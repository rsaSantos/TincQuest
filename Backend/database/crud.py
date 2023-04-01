from sqlalchemy.orm import Session

from . import models ,schemas

def create_user_from_user_create(user: schemas.UserCreate) -> models.User:
    return models.User(
        username=user.username,
        password=user.password,
        name=user.name,
        wallet_address=user.wallet_address,
    )

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()


def create_user(db: Session, user: schemas.UserCreate):
    db_user = create_user_from_user_create(user)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user