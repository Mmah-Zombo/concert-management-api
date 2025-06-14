from sqlalchemy.orm import Session
from models.play import Play
from schemas.play import PlayCreate
from datetime import datetime


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
