from sqlalchemy.orm import Session
from models.ticket import Ticket
from schemas.ticket import TicketRequestBody
from datetime import datetime


def get_all(db: Session):
    return db.query(Ticket).order_by(Ticket.id.asc()).all()


def get_by_id(ticket_id: int, db: Session):
    return db.query(Ticket).filter(Ticket.id == ticket_id).first()


def create(ticket: TicketRequestBody, db: Session):
    db_ticket = Ticket(**ticket.dict())
    db_ticket.created_at = datetime.utcnow()
    db_ticket.updated_at = datetime.utcnow()
    db.add(db_ticket)
    db.commit()
    db.refresh(db_ticket)
    return db_ticket


def update(ticket_id: int, ticket: TicketRequestBody, db: Session):
    db_ticket = get_by_id(ticket_id, db)
    if db_ticket:
        for key, value in ticket.dict(exclude_unset=True).items():
            setattr(db_ticket, key, value)
        db.commit()
        db.refresh(db_ticket)
    return db_ticket


def delete(ticket_id: int, db: Session):
    db_ticket = get_by_id(ticket_id, db)
    if db_ticket:
        db.delete(db_ticket)
        db.commit()
    return db_ticket