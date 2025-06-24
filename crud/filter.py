from datetime import datetime

from sqlalchemy.orm import Session
from models import actor, play, director, showtime



def filter_plays_by_genre(db: Session, genre: str):
    return db.query(play.Play).filter(play.Play.genre.ilike(f"%{genre}%")).all()



def filter_showtime_by_date(db: Session, start: datetime, end: datetime):
    return db.query(showtime.Showtime).filter(showtime.Showtime.date_time.between(start, end)).all()



def filter_actors_by_gender(db: Session, gender: str):
    return db.query(actor.Actor).filter(actor.Actor.gender.ilike(gender)).all()



def filter_directors_by_citizenship(db: Session, country: str):
    return db.query(director.Director).filter(director.Director.citizenship.ilike(f"%{country}%")).all()

