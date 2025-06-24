from sqlalchemy import Column, Integer, String, DateTime
from database import Base
from sqlalchemy.orm import relationship
from models.play import play_actors


class Actor(Base):
    __tablename__ = "actors"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    gender = Column(String, nullable=False)
    date_of_birth = Column(DateTime, nullable=False)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)

    plays = relationship("Play", secondary=play_actors, back_populates="actors")
