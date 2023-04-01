from typing import List
from pydantic import BaseModel

class QuestionBase(BaseModel):
    question :str

class QuestionCreate(QuestionBase):
    options : List[str]
    answer : str
    score : int

    class Config:
        orm_mode = True

class Question(QuestionBase):
    id : int
    options : List[str]
    answer : str
    score : int

    class Config:
        orm_mode = True
