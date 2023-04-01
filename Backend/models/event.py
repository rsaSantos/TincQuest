from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float, DateTime
from sqlalchemy.orm import relationship

from ..database.database import Base

class EventState:
    NEW = "NEW"
    OPEN = "OPEN"
    CLOSED = "CLOSED"

class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    private = Column(Boolean)
    max_registrations = Column(Integer)
    number_registrations = Column(Integer)
    entrance_fee = Column(Float)
    inicial_date = Column(DateTime)
    final_date = Column(DateTime)
    event_address = Column(String)
    event_state = Column(String)
    abi = Column(String)

    owner_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship("User", back_populates="ownedEvents")

    prize_id = Column(Integer, ForeignKey("prizes.id"))
    prize = relationship("Prize", uselist=False, back_populates="event")
    # participants = relationship("User", secondary="event_participants")