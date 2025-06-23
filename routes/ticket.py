from fastapi import APIRouter, Depends, HTTPException
from schemas.ticket import TicketResponse
from models.user import User
from dependencies.auth import get_current_user
from database import get_db
from sqlalchemy.orm import Session
from crud import ticket as ticket_crud
from crud.customer import get_by_id as get_customer
from crud.showtime import get_by_id as get_showtime
from schemas.ticket import TicketRequestBody


router = APIRouter(prefix="/tickets", tags=["Tickets"])


@router.get("/", response_model=list[TicketResponse])
def list_tickets(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return ticket_crud.get_all(db)


@router.post("/", response_model=TicketResponse)
def create_ticket(ticket: TicketRequestBody, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    showtime = get_showtime(ticket.showtime_id, db)
    if not showtime:
        raise HTTPException(status_code=404, detail=f"Showtime With id: {ticket.showtime_id} Not Found")

    customer = get_customer(ticket.customer_id, db)
    if not customer:
        raise HTTPException(status_code=404, detail=f"Customer With id: {ticket.customer_id} Not Found")

    return ticket_crud.create(ticket, db)


@router.get("/{ticket_id}", response_model=TicketResponse)
def get_ticket(ticket_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    ticket = ticket_crud.get_by_id(ticket_id, db)
    if not ticket:
        raise HTTPException(status_code=404, detail="Ticket Not Found")
    return ticket


@router.put("/{ticket_id}", response_model=TicketResponse)
def update_ticket(ticket_id: int, ticket: TicketRequestBody, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    showtime = get_showtime(ticket.showtime_id, db)
    if not showtime:
        raise HTTPException(status_code=404, detail=f"Showtime With id: {ticket.showtime_id} Not Found")

    customer = get_customer(ticket.customer_id, db)
    if not customer:
        raise HTTPException(status_code=404, detail=f"Customer With id: {ticket.customer_id} Not Found")

    ticket = ticket_crud.update(ticket_id, ticket, db)
    if not ticket:
        raise HTTPException(status_code=404, detail="Ticket Not Found")
    return ticket


@router.delete("/{ticket_id}")
def delete_ticket(ticket_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    ticket = ticket_crud.delete(ticket_id, db)
    if not ticket:
        raise HTTPException(status_code=404, detail="Ticket Not Found")
    return {"message": f"Ticket with id: {ticket_id} deleted"}