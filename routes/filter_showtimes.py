from datetime import datetime

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from crud.filter import filter_showtime_by_date

router = APIRouter(prefix="/showtimes", tags=["Showtimes"])


@router.get("/filter/date")
def filter_by_date(start: datetime, end: datetime, db: Session = Depends(get_db)):
    return filter_showtime_by_date(db, start, end)
