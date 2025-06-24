from sqlalchemy import Table, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

# Association tables
play_directors = Table(
    "play_directors",
    Base.metadata,
    Column("play_id", Integer, ForeignKey("plays.id")),
    Column("director_id", Integer, ForeignKey("directors.id")),
)

play_actors = Table(
    "play_actors",
    Base.metadata,
    Column("play_id", Integer, ForeignKey("plays.id")),
    Column("actor_id", Integer, ForeignKey("actors.id")),
)


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

    directors = relationship("Director", secondary=play_directors, back_populates="plays")
    actors = relationship("Actor", secondary=play_actors, back_populates="plays")
