from sqlalchemy import Column, Integer, String
from database import Base


class Play(Base):
    __tablename__ = "plays"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    genre = Column(String)
    description = Column(String)
