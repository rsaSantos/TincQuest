from typing import List, Tuple
from pydantic import BaseModel

class PrizeBase(BaseModel):
    base_prize : int
    registration_prize_percentage : float

class Prize(PrizeBase):
    distribution: List[int]

    class Config:
        orm_mode = True

class PrizeRead(PrizeBase):
    distribution: str

    class Config:
        orm_mode = True
