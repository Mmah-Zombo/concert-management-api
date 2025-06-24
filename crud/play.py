from sqlalchemy.orm import Session
from models.play import Play
from models.actor import Actor
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
