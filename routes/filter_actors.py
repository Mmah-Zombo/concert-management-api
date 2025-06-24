from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from crud import filter

router = APIRouter(prefix="/actors", tags=["Actors"])


@router.get("/filter/")
def filter_actor(gender: str, db: Session = Depends(get_db)):
    return filter.filter_actors_by_gender(db, gender)
