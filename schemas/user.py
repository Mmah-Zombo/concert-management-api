from pydantic import BaseModel
from datetime import datetime


class UserCreate(BaseModel):
    username: str
    password: str


class UserOut(BaseModel):
    id: int
    username: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class UserExit(BaseModel):
    id: int
    username: str


class Token(BaseModel):
    access_token: str
    token_type: str
