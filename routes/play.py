from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from schemas.play import PlayCreate, PlayOut, PlayActorAddResponse, ActorSummary, PlayActorRemoveResponse
from schemas.actor import ActorIDs
from schemas.director import DirectorIDs, DirectorSummary, PlayDirectorAddResponse, PlayDirectorRemoveResponse
from crud import play as play_crud
from crud import director as director_crud
from crud import actor as actor_crud
from dependencies.auth import get_current_user
from models.user import User
from typing import List


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


@router.post("/{play_id}/actors", response_model=PlayActorAddResponse)
def add_actors_to_play(play_id: int, actor_ids: ActorIDs, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    play = play_crud.get_by_id(db, play_id)
    if not play:
        raise HTTPException(status_code=404, detail="Play not found")

    actors = play_crud.get_actors(db, actor_ids)

    if not actors:
        raise HTTPException(status_code=404, detail="No valid actors found")

    added_actors = play_crud.add_actors(db, play, actors)

    if not added_actors:
        raise HTTPException(status_code=500, detail="Unable to add actors to play")

    return PlayActorAddResponse(
        play_title=play.title,
        added_actors=[ActorSummary(id=actor.id, name=actor.name) for actor in added_actors]
    )


@router.get("/{play_id}/actors", response_model=List[ActorSummary])
def get_actors_of_play(
    play_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    play = play_crud.get_by_id(db, play_id)
    if not play:
        raise HTTPException(status_code=404, detail="Play not found")

    return [
        ActorSummary(id=actor.id, name=actor.name)
        for actor in play.actors
    ]


@router.delete("/{play_id}/actors/{actor_id}")
def remove_actor_from_play(play_id: int, actor_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    play = play_crud.get_by_id(db, play_id)
    if not play:
        raise HTTPException(status_code=404, detail="Play not found")

    actor = actor_crud.get_by_id(actor_id, db)

    if not actor:
        raise HTTPException(status_code=404, detail="Actor not found")

    if actor not in play.actors:
        raise HTTPException(status_code=400, detail="Actor is not assigned to this play")

    play.actors.remove(actor)
    db.commit()

    return {"message": f"Actor with id: {actor_id} deleted from {play.title}"}


@router.post("/{play_id}/directors", response_model=PlayDirectorAddResponse)
def add_directors_to_play(
    play_id: int,
    director_ids: DirectorIDs,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    play = play_crud.get_by_id(db, play_id)
    if not play:
        raise HTTPException(status_code=404, detail="Play not found")

    directors = play_crud.get_directors(db, director_ids.director_ids)
    if not directors:
        raise HTTPException(status_code=404, detail="No valid directors found")

    added_directors = play_crud.add_directors(db, play, directors)
    if not added_directors:
        raise HTTPException(status_code=500, detail="Unable to add directors to play")

    return PlayDirectorAddResponse(
        play_title=play.title,
        added_directors=[
            DirectorSummary(id=director.id, name=director.name)
            for director in added_directors
        ]
    )


@router.get("/{play_id}/directors", response_model=List[DirectorSummary])
def get_directors_of_play(
    play_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    play = play_crud.get_by_id(db, play_id)
    if not play:
        raise HTTPException(status_code=404, detail="Play not found")

    return [
        DirectorSummary(id=director.id, name=director.name)
        for director in play.directors
    ]


@router.delete("/{play_id}/directors/{director_id}")
def remove_director_from_play(play_id: int, director_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    play = play_crud.get_by_id(db, play_id)
    if not play:
        raise HTTPException(status_code=404, detail="Play not found")

    director = director_crud.get_by_id(director_id, db)
    if not director:
        raise HTTPException(status_code=404, detail="Director not found")

    if director not in play.directors:
        raise HTTPException(status_code=400, detail="Director is not assigned to this play")

    play.directors.remove(director)
    db.commit()

    return {"message": f"Director with id: {director_id} deleted from {play.title}"}
