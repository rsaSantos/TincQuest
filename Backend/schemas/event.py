from datetime import datetime
from pydantic import BaseModel

from . import user as user_schema

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

    class Config:
        orm_mode = True