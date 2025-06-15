from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from database import Base


class Play(Base):
    __tablename__ = "plays"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    duration = Column(Integer, nullable=False)
    genre = Column(String, nullable=False)
    synopsis = Column(String)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)

    # One-to-Many: A Play has many ShowTimes
    showtimes = relationship(
        "Showtime",
        back_populates="play",
        cascade="all, delete-orphan",
        passive_deletes=True  # <== Important
    )
