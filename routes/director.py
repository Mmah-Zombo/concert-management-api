from fastapi import APIRouter, Depends, HTTPException
from crud import director as director_crud
from database import get_db
from dependencies.auth import get_current_user
from models.user import User
from schemas.director import DirectorResponse, DirectorRequestBody
from sqlalchemy.orm import Session


router = APIRouter(prefix="/directors", tags=["Directors"])


@router.get("/", response_model=list[DirectorResponse])
def list_directors(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return director_crud.get_all(db)


@router.post("/", response_model=DirectorResponse)
def create_director(director: DirectorRequestBody, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return director_crud.create(director, db)


@router.get("/{director_id}", response_model=DirectorResponse)
def get_director(director_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    director = director_crud.get_by_id(director_id, db)
    if not director:
        raise HTTPException(status_code=404, detail="Director Not Found")
    return director


@router.put("/{director_id}", response_model=DirectorResponse)
def update_director(director_id: int, director: DirectorRequestBody, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    director = director_crud.update(director_id, director, db)
    if not director:
        raise HTTPException(status_code=404, detail="Director Not Found")
    return director


@router.delete("/{director_id}")
def delete_director(director_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    director = director_crud.delete(director_id, db)
    if not director:
        raise HTTPException(status_code=404, detail="Director Not Found")
    return {"message": f"Director with id: {director_id} deleted"}
