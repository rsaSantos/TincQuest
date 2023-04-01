from sqlalchemy.orm import Session

from ..schemas import user as user_schema

from ..models import user as user_model

def create_user_from_user_create(user: user_schema.UserCreate) -> user_model.User:
    return user_model.User(
        username=user.username,
        password=user.password,
        name=user.name,
        wallet_address=user.wallet_address,
    )

def get_user(db: Session, user_id: int):
    return db.query(user_model.User).filter(user_model.User.id == user_id).first()


def get_user_by_username(db: Session, username: str):
    return db.query(user_model.User).filter(user_model.User.username == username).first()


def create_user(db: Session, user: user_schema.UserCreate):
    db_user = create_user_from_user_create(user)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user