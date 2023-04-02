import json
from sqlalchemy.orm import Session

from ..schemas import event as event_schema
from ..models import participant as participant_model
from ..models import event as event_model
from ..models import user as user_model
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
    or event.event_state != event_model.EventState.OPEN):
        return False
    event.number_registrations += 1
    participant = participant_model.Participant(
        score=0,
        answered_questions="[]",
        event_id=event_id,
        user_id=user_id
    )
    db.add(participant)
    db.commit()
    db.refresh(participant)
    return True

def get_event_participants(db: Session, event_id: int):
    return db.query(participant_model.Participant).filter(participant_model.Participant.event_id == event_id).join(
        user_model.User).order_by(participant_model.Participant.score.desc()).all()

def open_event(db: Session, event_id: int, user_id: int):
    event = get_event(db, event_id)
    if event.event_state != event_model.EventState.NEW or event.owner_id != user_id:
        return False
    event.event_state = event_model.EventState.OPEN
    db.commit()
    db.refresh(event)
    return True

def close_event(db: Session, event_id: int, user_id: int):
    event = get_event(db, event_id)
    if event.event_state != event_model.EventState.OPEN or event.owner_id != user_id:
        return False
    event.event_state = event_model.EventState.CLOSE
    db.commit()
    db.refresh(event)
    return True

def answer_quiz(db: Session, event_id: int, user_id: int, awnser: list):
    event = get_event(db, event_id)
    if event.event_state != event_model.EventState.OPEN:
        return False
    participant = db.query(participant_model.Participant).filter(participant_model.Participant.event_id == event_id, participant_model.Participant.user_id == user_id).first()
    if participant is None:
        return False
    for dict in awnser:
        question = db.query(question_crud.question_model.Question).filter(question_crud.question_model.Question.id == dict["id"]).first()
        if question is None:
            return False
        if question.answer == dict["awnser"]:
            participant.score += question.score
        participant.answered_questions = str(json.load(participant.answered_questions).append(dict["id"]))
    db.commit()
    db.refresh(participant)
    return True


