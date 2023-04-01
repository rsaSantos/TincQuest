from sqlalchemy.orm import Session

from ..schemas import participant as participant_schema
from ..models import participant as participant_model

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