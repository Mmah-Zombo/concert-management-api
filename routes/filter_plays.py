from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from crud import filter


router = APIRouter(prefix="/plays", tags=["Plays"])


@router.get("/filter/")
def filter_play(genre: str, db: Session = Depends(get_db)):
    return filter.filter_plays_by_genre(db, genre)
