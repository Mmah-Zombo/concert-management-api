from sqlalchemy import Column, String, Integer, DateTime
from database import Base
from sqlalchemy.orm import relationship
from models.play import play_directors


class Director(Base):
    __tablename__ = "directors"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    date_of_birth = Column(DateTime, nullable=False)
    citizenship = Column(String, nullable=False)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)

    plays = relationship("Play", secondary=play_directors, back_populates="directors")
