from sqlalchemy.orm import Session
from models.actor import Actor
from schemas.actor import ActorRequestBody
from datetime import datetime


def get_all(db: Session):
    return db.query(Actor).all()


def get_by_id(actor_id: int, db: Session):
    return db.query(Actor).filter(Actor.id == actor_id).first()


def create(actor: ActorRequestBody, db: Session):
    db_actor = Actor(**actor.dict())
    db_actor.created_at = datetime.utcnow()
    db_actor.updated_at = datetime.utcnow()
    db.add(db_actor)
    db.commit()
    db.refresh(db_actor)
    return db_actor


def update(actor_id: int, actor: ActorRequestBody, db: Session):
    db_actor = get_by_id(actor_id, db)
    if db_actor:
        for key, value in actor.dict().items():
            setattr(db_actor, key, value)
        db.commit()
        db.refresh(db_actor)
    return db_actor


def delete(actor_id: int, db: Session):
    db_actor = get_by_id(actor_id, db)
    if db_actor:
        db.delete(db_actor)
        db.commit()
    return db_actor
