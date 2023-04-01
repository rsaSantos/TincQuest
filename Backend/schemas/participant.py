from typing import List
from pydantic import BaseModel

class ParticipantBase(BaseModel):
    id: int

class Participant(ParticipantBase):
    score : int
    awsered_questions: List[int]

    class Config:
        orm_mode = True

class ParticipantRead(ParticipantBase):
    score : int
    awsered_questions: str

    class Config:
        orm_mode = True