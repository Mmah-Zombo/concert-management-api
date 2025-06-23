from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.orm import relationship
from database import Base


class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    telephone_no = Column(String, nullable=False)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)

    tickets = relationship("Ticket", back_populates="customer", cascade="all, delete-orphan", passive_deletes=True)