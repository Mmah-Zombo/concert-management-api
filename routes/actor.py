from fastapi import APIRouter, Depends, HTTPException
from schemas.actor import ActorResponse
from models.user import User
from dependencies.auth import get_current_user
from database import get_db
from sqlalchemy.orm import Session
from crud import actor as actor_crud
from schemas.actor import ActorRequestBody


router = APIRouter(prefix="/actors", tags=["Actors"])


@router.get("/", response_model=list[ActorResponse])
def list_actors(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return actor_crud.get_all(db)


@router.post("/", response_model=ActorResponse)
def create_actor(actor: ActorRequestBody, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return actor_crud.create(actor, db)


@router.get("/{actor_id}", response_model=ActorResponse)
def get_actor(actor_id: int, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    actor = actor_crud.get_by_id(actor_id, db)
    if not actor:
        raise HTTPException(status_code=404, detail="Actor Not Found")
    return actor


@router.put("/{actor_id}", response_model=ActorResponse)
def update_actor(actor_id: int, actor: ActorRequestBody, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    actor = actor_crud.update(actor_id, actor, db)
    if not actor:
        raise HTTPException(status_code=404, detail="Actor Not Found")
    return actor


@router.delete("/{actor_id}")
def delete_actor(actor_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    actor = actor_crud.delete(actor_id, db)
    if not actor:
        raise HTTPException(status_code=404, detail="Actor Not Found")
    return {"message": f"Actor with id: {actor_id} deleted"}
