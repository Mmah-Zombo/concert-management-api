from fastapi import APIRouter, Depends, HTTPException
from schemas.showtime import ShowtimeResponse
from models.user import User
from dependencies.auth import get_current_user
from database import get_db
from sqlalchemy.orm import Session
from crud import showtime as showtime_crud
from crud.play import get_by_id as get_play
from schemas.showtime import ShowtimeRequestBody


router = APIRouter(prefix="/showtimes", tags=["Showtimes"])


@router.get("/", response_model=list[ShowtimeResponse])
def list_showtimes(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return showtime_crud.get_all(db)


@router.post("/", response_model=ShowtimeResponse)
def create_showtime(showtime: ShowtimeRequestBody, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    play = get_play(db, showtime.play_id)
    if not play:
        raise HTTPException(status_code=404, detail=f"Play With id: {showtime.play_id} Not Found")
    return showtime_crud.create(showtime, db)


@router.get("/{showtime_id}", response_model=ShowtimeResponse)
def get_showtime(showtime_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    showtime = showtime_crud.get_by_id(showtime_id, db)
    if not showtime:
        raise HTTPException(status_code=404, detail="Showtime Not Found")
    return showtime


@router.put("/{showtime_id}", response_model=ShowtimeResponse)
def update_showtime(showtime_id: int, showtime: ShowtimeRequestBody, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    play = get_play(db, showtime.play_id)
    if not play:
        raise HTTPException(status_code=404, detail=f"Play With id: {showtime.play_id} Not Found")
    showtime = showtime_crud.update(showtime_id, showtime, db)
    if not showtime:
        raise HTTPException(status_code=404, detail="Showtime Not Found")
    return showtime


@router.delete("/{showtime_id}")
def delete_showtime(showtime_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    showtime = showtime_crud.delete(showtime_id, db)
    if not showtime:
        raise HTTPException(status_code=404, detail="Showtime Not Found")
    return {"message": f"Showtime with id: {showtime_id} deleted"}
