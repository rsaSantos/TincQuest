from sqlalchemy.orm import Session

from ..schemas import event as event_schema
from ..models import participant as participant_model
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
        number_registrations=0,
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

def get_my_events(db: Session, user_id: int):
    return db.query(event_model.Event).join(participant_model.Participant).filter(participant_model.Participant.user_id == user_id).all()

def get_events(db: Session, user_id : int):
    event_list = db.query(event_model.Event).filter(event_model.Event.private == False).all()
    event_list.extend(get_my_events(db, user_id))
    event_list.extend(get_owned_events(db, user_id))
    return list(set(event_list))

def join_event(db : Session, event_id : int, user_id : int):
    event = get_event(db, event_id)
    if (user_id in [k.user_id for k in event.participants] 
    or event.number_registrations >= event.max_registrations 
    or event.owner_id == user_id
    or event.event_state == event_model.EventState.OPEN):
        print(event.number_registrations)
        print(event.max_registrations)
        print(event.owner_id)
        print(event.event_state)
        print(user_id)
        return False
    event.number_registrations += 1
    participant = participant_model.Participant(
        score=0,
        awsered_questions="[]",
        event_id=event_id,
        user_id=user_id
    )
    db.add(participant)
    db.commit()
    db.refresh(participant)
    return True


