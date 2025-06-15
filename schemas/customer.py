from pydantic import BaseModel
from datetime import datetime


class CustomerRequestBody(BaseModel):
    name: str
    telephone_no: str


class CustomerResponse(BaseModel):
    id: int
    name: str
    telephone_no: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
