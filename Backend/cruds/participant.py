from sqlalchemy.orm import Session

from ..schemas import participant as participant_schema
from ..models import participant as participant_model
from ..models import user as user_model

def create_participant_from_participant_create(participant: participant_schema.ParticipantBase) -> participant_model.Participant:
    return participant_model.Participant(
        score=participant.score,
        awsered_questions=str(participant.awsered_questions),
    )

def create_question(db: Session,participant: participant_schema.ParticipantBase):
    db_participant = create_participant_from_participant_create(participant)
    db.add(db_participant)
    db.commit()
    db.refresh(db_participant)
    return db_participant

def get_participant_winner(db: Session, event_id: int, n: int):
    all_winner = db.query(participant_model.Participant).filter(participant_model.Participant.event_id == event_id).join(
        user_model.User).order_by(participant_model.Participant.score.desc()).all()
    return all_winner[:n]
