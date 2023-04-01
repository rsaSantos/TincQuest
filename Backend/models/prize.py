from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship

from ..database.database import Base

class Prize(Base):
    __tablename__ = "prizes"

    id = Column(Integer, primary_key=True, index=True)
    base_prize = Column(Integer)
    registration_prize_percentage = Column(Float)
    distribution = Column(String)

    event = relationship("Event", back_populates="prize")

