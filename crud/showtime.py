from sqlalchemy.orm import Session
from models.showtime import Showtime
from schemas.showtime import ShowtimeRequestBody
from datetime import datetime


def get_all(db: Session):
    return db.query(Showtime).order_by(Showtime.id.asc()).all()


def get_by_id(showtime_id: int, db: Session):
    return db.query(Showtime).filter(Showtime.id == showtime_id).first()


def create(showtime: ShowtimeRequestBody, db: Session):
    db_showtime = Showtime(**showtime.dict())
    db_showtime.created_at = datetime.utcnow()
    db_showtime.updated_at = datetime.utcnow()
    db.add(db_showtime)
    db.commit()
    db.refresh(db_showtime)
    return db_showtime


def update(showtime_id: int, showtime: ShowtimeRequestBody, db: Session):
    db_showtime = get_by_id(showtime_id, db)
    if db_showtime:
        for key, value in showtime.dict(exclude_unset=True).items():
            setattr(db_showtime, key, value)
        db.commit()
        db.refresh(db_showtime)
    return db_showtime


def delete(showtime_id: int, db: Session):
    db_showtime = get_by_id(showtime_id, db)
    if db_showtime:
        db.delete(db_showtime)
        db.commit()
    return db_showtime
