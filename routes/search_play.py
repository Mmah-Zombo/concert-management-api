from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from crud import search


router = APIRouter(prefix="/plays", tags=["Plays"])

@router.get("/search/")
def search_play(title: str, db: Session = Depends(get_db)):
    return search.search_plays_by_title(db, title)