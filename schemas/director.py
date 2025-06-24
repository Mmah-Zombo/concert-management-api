from pydantic import BaseModel
from datetime import datetime
from typing import List


class DirectorRequestBody(BaseModel):
    name: str
    date_of_birth: datetime
    citizenship: str


class DirectorResponse(BaseModel):
    id: int
    name: str
    date_of_birth: datetime
    citizenship: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class DirectorIDs(BaseModel):
    director_ids: List[int]


class DirectorSummary(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True


class PlayDirectorAddResponse(BaseModel):
    play_title: str
    added_directors: List[DirectorSummary]


class PlayDirectorRemoveResponse(BaseModel):
    play_title: str
    removed_directors: List[DirectorSummary]
