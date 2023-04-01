from pydantic import BaseModel

class UserBase(BaseModel):
    username: str

class UserLogin(UserBase):
    password: str

class UserCreate(UserBase):
    name: str
    password: str
    wallet_address: str


class User(UserBase):
    name: str

    class Config:
        orm_mode = True