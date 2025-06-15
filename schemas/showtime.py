from pydantic import BaseModel
from datetime import datetime


class ShowtimeRequestBody(BaseModel):
    date_time: datetime
    play_id: int


class ShowtimeResponse(BaseModel):
    id: int
    date_time: datetime
    play_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
