from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class Ticket(Base):
    __tablename__ = "tickets"

    # id = Column(Integer, primary_key=True, index=True)
    # seat_no = Column(Integer, nullable=False)
    # seat_row = Column(Integer, nullable=False)
    # ticket_no = Column(Integer, nullable=False)
    # showtime_id = Column(Integer, ForeignKey("showtimes.id"), nullable=False)
    # customer_id = Column(Integer, ForeignKey("customers.id"), nullable=False)
    # created_at = Column(DateTime, nullable=False)
    # updated_at = Column(DateTime, nullable=False)
    #
    # # Many-to-One: Each ticket belongs to one customer
    # customer = relationship("Customer", back_populates="tickets")


