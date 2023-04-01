from sqlalchemy.orm import Session

from ..schemas import prize as prize_schema
from ..models import prize as prize_model

def create_prize_from_prize_create(prize: prize_schema.Prize) -> prize_model.Prize:
    return prize_model.Prize(
        base_prize=prize.base_prize,
        registration_prize_percentage=prize.registration_prize_percentage,
        distribution=str(prize.distribution),
    )

def create_prize(db: Session, prize: prize_schema.Prize):
    db_prize = create_prize(prize)
    db.add(db_prize)
    db.commit()
    db.refresh(db_prize)
    return db_prize