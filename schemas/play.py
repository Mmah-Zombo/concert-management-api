from pydantic import BaseModel
from datetime import datetime
from typing import List


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


class ActorSummary(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True


class PlayActorAddResponse(BaseModel):
    play_title: str
    added_actors: List[ActorSummary]
