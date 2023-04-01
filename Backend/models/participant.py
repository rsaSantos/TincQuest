from sqlalchemy import Column, ForeignKey, Integer , String
from sqlalchemy.orm import relationship

from ..database.database import Base

class Participant(Base):
    __tablename__ = "participants"

    id = Column(Integer, primary_key=True, index=True)
    score = Column(Integer)
    awsered_questions = Column(String)

    user_id = Column(Integer, ForeignKey("users.id"))
    event_id = Column(Integer, ForeignKey("events.id"))
    user = relationship("User", back_populates="participations")
    event = relationship("Event", back_populates="participants")
