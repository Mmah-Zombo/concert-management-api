from pydantic import BaseModel
from datetime import datetime


class ActorRequestBody(BaseModel):
    name: str
    gender: str
    date_of_birth: datetime


class ActorResponse(BaseModel):
    id: int
    name: str
    gender: str
    date_of_birth: datetime
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
