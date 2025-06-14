from pydantic import BaseModel
from datetime import datetime


class PlayBase(BaseModel):
    title: str
    duration: int
    genre: str
    synopsis: str = None


class PlayCreate(PlayBase):
    pass


class PlayOut(BaseModel):
    id: int
    title: str
    duration: int
    genre: str
    synopsis: str = None
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
