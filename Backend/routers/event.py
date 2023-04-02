import json
from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from Backend.auth.auth import get_current_user
from Backend.routers.web3 import get_abi
from ..schemas import event as event_schema
from ..schemas import user as user_schema
from ..schemas import participant as participant_schema
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
            p.answered_questions = json.loads(p.answered_questions)
            
    if event.questions:
        for q in event.questions:
            q.options = eval(q.options)
    return event

def correct_answered_questions(participant):
    participant.answered_questions = json.loads(participant.answered_questions)
    return participant

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
    event = event_crud.get_event(db, event_id)
    if not event:
        raise HTTPException(status_code=404, detail="event not found")
    event = correct(event)
    if event.event_state != event_model.EventState.OPEN:
        event.questions = []
    if event.participants:
        for p in event.participants:
            if p.user_id == current_user.id:
                event.questions = list(filter(lambda q:q.id not in p.answered_questions, event.questions))
                return event
    if event.owner_id == current_user.id or event.private == False:
        return event
    raise HTTPException(status_code=400, detail="user is not part of event")
    
@event_router.post("/event")
def create_event(event: event_schema.EventCreate, current_user: Annotated[user_schema.User, Depends(get_current_user)], db: Session = Depends(get_db)):
    event_crud.create_event(db, event, current_user.id)

@event_router.put("/joinEvent/{event_id}", response_model=event_schema.EventDetail)
def join_event(event_id : int, current_user: Annotated[user_schema.User, Depends(get_current_user)], db: Session = Depends(get_db)):
    event = event_crud.join_event(db, event_id, current_user.id)
    if not event:
        raise HTTPException(status_code=400, detail="user can´t join event")
    return correct(event)

@event_router.get("/event/leaderboard/{event_id}", response_model=list[participant_schema.ParticipantUser])
def get_leaderboard(event_id : int, current_user: Annotated[user_schema.User, Depends(get_current_user)], db: Session = Depends(get_db)):
    return [correct_answered_questions(e) for e in event_crud.get_event_participants(db, event_id)]

@event_router.put("/openEvent/{event_id}", response_model=event_schema.EventDetail)
def open_event(event_id : int, current_user: Annotated[user_schema.User, Depends(get_current_user)], db: Session = Depends(get_db)):
    event = event_crud.open_event(db, event_id, current_user.id)
    if not event:
        raise HTTPException(status_code=400, detail="user can´t open event")
    return correct(event)

@event_router.put("/event/terminate/{event_id}", response_model=event_schema.EventDetail)
def terminate_event(event_id : int, current_user: Annotated[user_schema.User, Depends(get_current_user)], db: Session = Depends(get_db)):
    # Get ABI and event contract address
    ABI = get_abi()
    contract_address = event_crud.get_event(db, event_id).event_address

    # Terminate the event in the blockchain
    if(web3_event.terminate_event( db, ABI, contract_address , event_id)):
        event = event_crud.close_event(db, event_id, current_user.id)
        if not event:
            raise HTTPException(status_code=400, detail="user can´t close event")
        return correct(event)
    
    raise HTTPException(status_code=400, detail="blockchain error")
        
@event_router.put("/answer_quiz/{event_id}")
def answer_quiz(event_id : int, answer: list, current_user: Annotated[user_schema.User, Depends(get_current_user)], db: Session = Depends(get_db)):
    event_crud.answer_quiz(db, event_id, current_user.id, answer)