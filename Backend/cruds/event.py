from sqlalchemy.orm import Session

from ..schemas import event as event_schema
from ..models import event as event_model
from ..cruds import prize as prize_crud
from ..cruds import question as question_crud

def create_event_from_event_create(db: Session, event: event_schema.EventCreate, owner_id: int) -> event_model.Event:
    prize = prize_crud.create_prize(db, event.prize)
    questions = [question_crud.create_question(db, q) for q in event.questions]
    return event_model.Event(
        name=event.name,
        description=event.description,
        private=event.private,
        max_registrations=event.max_registrations,
        number_registrations=event.number_registrations,
        entrance_fee=event.entrance_fee,
        inicial_date=event.inicial_date,
        final_date=event.final_date,
        event_address=event.event_address,
        event_state=event_model.EventState.NEW,
        owner_id=owner_id,
        prize=prize,
        prize_id=prize.id,
        abi=event.abi,
        questions=questions
    )

def get_owned_events(db: Session, owner_id: int):
    return db.query(event_model.Event).filter(event_model.Event.owner_id == owner_id).all()

def get_event(db: Session, event_id: int):
    return db.query(event_model.Event).filter(event_model.Event.id == event_id).first()


def create_event(db: Session, event: event_schema.EventCreate, owner_id: int):
    db_event = create_event_from_event_create(db, event, owner_id)
    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    return get_event(db, db_event.id)
