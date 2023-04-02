import json
from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from Backend.auth.auth import get_current_user
from ..schemas import event as event_schema
from ..schemas import user as user_schema
from ..cruds import event as event_crud

from ..models import event as event_model
from ..models import prize as prize_model
from ..web3 import web3_event

from Backend.dependencies import get_db

event_router = FastAPI()

def correct(event):
    if event.prize.distribution:
        event.prize.distribution = json.loads(event.prize.distribution)
    if event.participants:
        for p in event.participants:
            p.awsered_questions = json.loads(p.awsered_questions)
    if event.questions:
        for q in event.questions:
            q.options = eval(q.options)
    return event

@event_router.get("/myevents", response_model=list[event_schema.EventBasic])
def get_my_events(current_user: Annotated[user_schema.User, Depends(get_current_user)], db: Session = Depends(get_db)):
    return [correct(e) for e in event_crud.get_my_events(db, current_user.id)]

@event_router.get("/ownedEvents", response_model=list[event_schema.EventBasic])
def get_owned_events(current_user: Annotated[user_schema.User, Depends(get_current_user)], db: Session = Depends(get_db)):
    return [correct(e) for e in event_crud.get_owned_events(db, current_user.id)]

@event_router.get("/events", response_model=list[event_schema.EventBasic])
def get_events(current_user: Annotated[user_schema.User, Depends(get_current_user)], db: Session = Depends(get_db)):
    return [correct(e) for e in event_crud.get_events(db, current_user.id)]

@event_router.get("/event/{event_id}", response_model=event_schema.EventDetail)
def get_event(event_id : int, current_user: Annotated[user_schema.User, Depends(get_current_user)], db: Session = Depends(get_db)):
    event = correct(event_crud.get_event(db, event_id))
    if event.event_state != event_model.EventState.OPEN:
        event.questions = []
    if event.participants:
        for p in event.participants:
            if p.user_id == current_user.id:
                return event
    elif event.owner_id == current_user.id:
        return event
    raise HTTPException(status_code=400, detail="user is not part of event")
    
@event_router.post("/event")
def create_event(event: event_schema.EventCreate, current_user: Annotated[user_schema.User, Depends(get_current_user)], db: Session = Depends(get_db)):
    event_crud.create_event(db, event, current_user.id)

@event_router.put("/joinEvent/{event_id}")
def join_event(event_id : int, current_user: Annotated[user_schema.User, Depends(get_current_user)], db: Session = Depends(get_db)):
    if not event_crud.join_event(db, event_id, current_user.id):
        raise HTTPException(status_code=400, detail="user can´t join event")

@event_router.post("/event/terminate/{event_id}", response_model=bool)
def terminate_event(event_id : int, current_user: Annotated[user_schema.User, Depends(get_current_user)], db: Session = Depends(get_db)):
    # Get ABI and event contract address
    ABI = event_crud.get_event(db, event_id).abi
    contract_address = event_crud.get_event(db, event_id).event_address

    # Terminate the event in the blockchain
    if(web3_event.terminate_event( db, ABI, contract_address , event_id)):
        # TODO: 
        # 1. Alterar o estado do evento para terminado
        return True
    else:
        return False