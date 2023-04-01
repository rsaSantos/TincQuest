from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Double, DateTime, Table
from sqlalchemy.orm import relationship

from ..database.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    username = Column(String, unique=True, index=True)
    password = Column(String)
    wallet_address = Column(String, unique=True, index=True)

    # joinedEvents
    # ownedEvents = relationship("Event", back_populates="owner")

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
    entrance_fee = Column(Double)
    inicial_date = Column(DateTime)
    final_date = Column(DateTime)
    event_address = Column(String)
    event_state = Column(String)

    # owner = relationship("User", back_populates="ownedEvents")
    # participants = relationship("User", secondary="event_participants")