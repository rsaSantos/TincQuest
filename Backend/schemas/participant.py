from typing import List
from pydantic import BaseModel
from ..schemas import user as user_schema

class ParticipantBase(BaseModel):
    id: int

class Participant(ParticipantBase):
    score : int
    answered_questions: List[int]

    class Config:
        orm_mode = True

class ParticipantInfo(BaseModel):
    score : int
    answered_questions: List[int]
    user_id: int

    class Config:
        orm_mode = True

class ParticipantUser(BaseModel):
    score : int
    answered_questions: List[int]
    user_id: int
    user: user_schema.User

    class Config:
        orm_mode = True

class ParticipantWinner(ParticipantBase):
    score : int
    answered_questions: str
    wallet_address: str

    class Config:
        orm_mode = True