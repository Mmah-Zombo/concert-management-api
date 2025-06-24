from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from crud import filter


router = APIRouter(prefix="/directors", tags=["Directors"])


@router.get("/filter/")
def filter_director(citizenship: str, db: Session = Depends(get_db)):
    return filter.filter_directors_by_citizenship(db, citizenship)


