from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from ..database.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    username = Column(String, unique=True, index=True)
    password = Column(String)
    wallet_address = Column(String, unique=True, index=True)

    ownedEvents = relationship("Event", back_populates="owner")
    participations = relationship("Participant", back_populates="user")
