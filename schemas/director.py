from pydantic import BaseModel
from datetime import datetime


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

