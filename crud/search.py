from sqlalchemy.orm import Session
from models import actor, play, director

def search_actors_by_name(db: Session, keyword: str):
    return db.query(actor.Actor).filter(actor.Actor.name.ilike(f"%{keyword}%")).all()



def search_directors_by_name(db: Session, keyword: str):
    return db.query(director.Director).filter(director.Director.name.ilike(f"%{keyword}%")).all()



def search_plays_by_title(db: Session, keyword: str):
    return db.query(play.Play).filter(play.Play.title.ilike(f"%{keyword}%")).all()

