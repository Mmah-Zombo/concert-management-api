from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from crud import search

router = APIRouter(prefix="/actors", tags=["Actors"])


@router.get("/search/")
def search_actor(name: str, db: Session = Depends(get_db)):
    return search.search_actors_by_name(db, name)
