from datetime import datetime
from models.director import Director
from schemas.director import DirectorRequestBody
from sqlalchemy.orm import Session


def get_all(db: Session):
    return db.query(Director).order_by(Director.id.asc()).all()


def get_by_id(director_id: int, db: Session):
    return db.query(Director).filter(Director.id == director_id).first()


def create(director: DirectorRequestBody, db: Session):
    db_director = Director(**director.dict())
    db_director.created_at = datetime.utcnow()
    db_director.updated_at = datetime.utcnow()
    db.add(db_director)
    db.commit()
    db.refresh(db_director)
    return db_director


def update(director_id: int, director: DirectorRequestBody, db: Session):
    db_director = get_by_id(director_id, db)
    if db_director:
        for key, value in director.dict(exclude_unset=True).items():
            setattr(db_director, key, value)
        db_director.updated_at = datetime.utcnow()
        db.commit()
        db.refresh(db_director)
    return db_director


def delete(director_id: int, db: Session):
    db_director = get_by_id(director_id, db)
    if db_director:
        db.delete(db_director)
        db.commit()
    return db_director
