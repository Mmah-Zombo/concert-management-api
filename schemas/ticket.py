from pydantic import BaseModel
from datetime import datetime


class TicketRequestBody(BaseModel):
    price: float
    seat_no: int
    seat_row: int
    ticket_no: int
    showtime_id: int
    customer_id: int


class TicketResponse(BaseModel):
    id: int
    price: float
    seat_no: int
    seat_row: int
    ticket_no: int
    showtime_id: int
    customer_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


