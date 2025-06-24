from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from crud import search

router = APIRouter(prefix="/directors", tags=["Directors"])

@router.get("/search/")
def search_director(name: str, db: Session = Depends(get_db)):
    return search.search_directors_by_name(db, name)
