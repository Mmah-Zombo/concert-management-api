from sqlalchemy.orm import Session
from models.customer import Customer
from schemas.customer import CustomerRequestBody
from datetime import datetime


def get_all(db: Session):
    return db.query(Customer).order_by(Customer.id.asc()).all()


def get_by_id(customer_id: int, db: Session):
    return db.query(Customer).filter(Customer.id == customer_id).first()


def create(customer: CustomerRequestBody, db: Session):
    db_customer = Customer(**customer.dict())
    db_customer.created_at = datetime.utcnow()
    db_customer.updated_at = datetime.utcnow()
    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)
    return db_customer


def update(customer_id: int, customer: CustomerRequestBody, db: Session):
    db_customer = get_by_id(customer_id, db)
    if db_customer:
        for key, value in customer.dict(exclude_unset=True).items():
            setattr(db_customer, key, value)
        db.commit()
        db.refresh(db_customer)
    return db_customer


def delete(customer_id: int, db: Session):
    db_customer = get_by_id(customer_id, db)
    if db_customer:
        db.delete(db_customer)
        db.commit()
    return db_customer
