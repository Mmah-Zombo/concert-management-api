from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class Showtime(Base):
    __tablename__ = "showtimes"

    id = Column(Integer, primary_key=True, index=True)
    date_time = Column(DateTime, nullable=False, unique=True)
    play_id = Column(Integer, ForeignKey("plays.id", ondelete="CASCADE"), nullable=False)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)

    # Many-to-One: ShowTime belongs to one Play
    play = relationship("Play", back_populates="showtimes")
    tickets = relationship("Ticket", back_populates="showtime", cascade="all, delete-orphan", passive_deletes=True)