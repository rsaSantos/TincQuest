from datetime import datetime
from pydantic import BaseModel

from . import user as user_schema
from . import prize as prize_schema

class EventBase(BaseModel):
    name: str

class EventCreate(EventBase):
    description: str
    private: bool
    max_registrations: int
    number_registrations: int
    entrance_fee: float
    inicial_date: datetime
    final_date: datetime
    prize: prize_schema.Prize


class EventOwned(EventBase):
    id: int
    description: str
    private: bool
    max_registrations: int
    number_registrations: int
    entrance_fee: float
    inicial_date: datetime
    final_date: datetime
    event_address: str
    event_state: str
    owner_id: int
    owner: user_schema.User
    prize: prize_schema.Prize

    class Config:
        orm_mode = True