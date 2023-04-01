from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from ..database.database import Base

class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True, index=True)
    question = Column(String)
    options = Column(String)
    answer = Column(String)
    score = Column(Integer)

    event_id = Column(Integer, ForeignKey("events.id"))
    event = relationship("Event", back_populates="questions")
