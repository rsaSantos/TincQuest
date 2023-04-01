from sqlalchemy.orm import Session

from ..schemas import question as question_schema
from ..models import question as question_model

def create_question_from_question_create(question: question_schema.QuestionCreate) -> question_model.Question:
    return question_model.Question(
        question=question.question,
        options=str(question.options),
        answer=question.answer,
        score=question.score,
    )

def create_question(db: Session, question : question_schema.QuestionCreate):
    db_create = create_question_from_question_create(question)
    db.add(db_create)
    db.commit()
    db.refresh(db_create)
    return db_create