from datetime import datetime
from pydantic import BaseModel

from . import user as user_schema
from . import prize as prize_schema
from . import participant as participant_schema
from . import question as question_schema

class EventBase(BaseModel):
    name: str

class EventBasic(EventBase):
    id: int
    max_registrations: int
    number_registrations: int
    inicial_date: datetime
    final_date: datetime
    prize: prize_schema.Prize

    class Config:
        orm_mode = True

class EventCreate(EventBase):
    description: str
    private: bool
    max_registrations: int
    entrance_fee: float
    inicial_date: datetime
    final_date: datetime
    event_address: str
    abi:str
    prize: prize_schema.Prize
    questions: list[question_schema.QuestionCreate]

class EventDetail(EventBase):
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
    
    owner: user_schema.User
    prize: prize_schema.Prize
    participants: list[participant_schema.Participant]
    questions: list[question_schema.Question]

    class Config:
        orm_mode = True