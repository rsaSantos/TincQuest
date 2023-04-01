import json
from typing import Annotated

from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session
from Backend.auth.auth import get_current_user
from ..schemas import event as event_schema
from ..schemas import user as user_schema
from ..cruds import event as event_crud
from ..models import event as event_model
from ..models import prize as prize_model

from Backend.dependencies import get_db

from ..database.database import engine

event_model.Base.metadata.create_all(bind=engine)
prize_model.Base.metadata.create_all(bind=engine)


event_router = FastAPI()

def correct_prize(event):
    event.prize.distribution = json.loads(event.prize.distribution)
    return event


@event_router.post("/event", response_model=event_schema.EventOwned)
def create_event(event: event_schema.EventCreate, current_user: Annotated[user_schema.User, Depends(get_current_user)], db: Session = Depends(get_db)):
    return correct_prize(event_crud.create_event(db, event, current_user.id))

@event_router.get("/ownedEvent", response_model=list[event_schema.EventOwned])
def get_owned_events(current_user: Annotated[user_schema.User, Depends(get_current_user)], db: Session = Depends(get_db)):
    return event_crud.get_owned_events(db, current_user.id)

@event_router.get("/event/{event_id}", response_model=event_schema.EventDetail)
def get_event(event_id : int, current_user: Annotated[user_schema.User, Depends(get_current_user)], db: Session = Depends(get_db)):
    # More checks
    return correct_prize(event_crud.get_event(db, event_id))
