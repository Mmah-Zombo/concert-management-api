from sqlalchemy.orm import Session
from models.play import Play
from models.actor import Actor
from models.director import Director
from schemas.play import PlayCreate, PlayOut
from schemas.actor import ActorIDs
from datetime import datetime
from typing import List


def get_all(db: Session):
    return db.query(Play).order_by(Play.id.asc()).all()


def get_by_id(db: Session, play_id: int):
    return db.query(Play).filter(Play.id == play_id).first()


def create(db: Session, play: PlayCreate):
    db_play = Play(**play.dict())
    db_play.created_at = datetime.utcnow()
    db_play.updated_at = datetime.utcnow()
    db.add(db_play)
    db.commit()
    db.refresh(db_play)
    return db_play


def update(db: Session, play_id: int, play: PlayCreate):
    db_play = get_by_id(db, play_id)
    if db_play:
        db_play.updated_at = datetime.utcnow()
        for key, value in play.dict(exclude_unset=True).items():
            setattr(db_play, key, value)
        db.commit()
        db.refresh(db_play)
    return db_play


def delete(db: Session, play_id: int):
    db_play = get_by_id(db, play_id)
    if db_play:
        db.delete(db_play)
        db.commit()
    return db_play


def get_actors(db: Session, actor_ids: ActorIDs):
    return db.query(Actor).filter(Actor.id.in_(actor_ids.actor_ids)).all()


def add_actors(db: Session, play: PlayOut, actors: List[Actor]):
    existing_ids = {actor.id for actor in play.actors}
    new_actors = [actor for actor in actors if actor.id not in existing_ids]

    play.actors.extend(new_actors)
    db.commit()
    db.refresh(play)

    return new_actors


def remove_actors(db: Session, play: Play, actor_ids: List[int]):
    actors_to_remove = db.query(Actor).filter(Actor.id.in_(actor_ids)).all()
    for actor in actors_to_remove:
        if actor in play.actors:
            play.actors.remove(actor)
    db.commit()
    return actors_to_remove


def get_directors(db: Session, ids: List[int]):
    return db.query(Director).filter(Director.id.in_(ids)).all()


def add_directors(db: Session, play: Play, directors: List[Director]):
    existing_ids = {d.id for d in play.directors}
    new_directors = [d for d in directors if d.id not in existing_ids]
    play.directors.extend(new_directors)
    db.commit()
    db.refresh(play)
    return new_directors


def remove_directors(db: Session, play: Play, director_ids: List[int]):
    directors_to_remove = db.query(Director).filter(Director.id.in_(director_ids)).all()
    for director in directors_to_remove:
        if director in play.directors:
            play.directors.remove(director)
    db.commit()
    return directors_to_remove
