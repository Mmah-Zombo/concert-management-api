from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from schemas.play import PlayCreate, PlayOut
from crud import play as play_crud
from dependencies.auth import get_current_user
from models.user import User

router = APIRouter(prefix="/plays", tags=["Plays"])


@router.post("/", response_model=PlayOut)
def create_play(play: PlayCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return play_crud.create(db, play)


@router.get("/", response_model=list[PlayOut])
def list_plays(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return play_crud.get_all(db)


@router.get("/{play_id}", response_model=PlayOut)
def get_play(play_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    play = play_crud.get_by_id(db, play_id)
    if not play:
        raise HTTPException(status_code=404, detail="Play not found")
    return play


@router.put("/{play_id}", response_model=PlayOut)
def update_play(play_id: int, play: PlayCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    play = play_crud.update(db, play_id, play)
    if not play:
        raise HTTPException(status_code=404, detail="Play Not Found")
    return play


@router.delete("/{play_id}")
def delete_play(play_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    play = play_crud.delete(db, play_id)
    if not play:
        raise HTTPException(status_code=404, detail="Play not found")
    return {"message": f"Showtime with id: {play_id} deleted"}
