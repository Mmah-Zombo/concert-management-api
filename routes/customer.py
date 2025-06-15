from fastapi import APIRouter, Depends, HTTPException
from schemas.customer import CustomerResponse
from models.user import User
from dependencies.auth import get_current_user
from database import get_db
from sqlalchemy.orm import Session
from crud import customer as customer_crud
from schemas.customer import CustomerRequestBody


router = APIRouter(prefix="/customers", tags=["Customers"])


@router.get("/", response_model=list[CustomerResponse])
def list_customers(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return customer_crud.get_all(db)


@router.post("/", response_model=CustomerResponse)
def create_customer(customer: CustomerRequestBody, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return customer_crud.create(customer, db)


@router.get("/{customer_id}", response_model=CustomerResponse)
def get_customer(customer_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    customer = customer_crud.get_by_id(customer_id, db)
    if not customer:
        raise HTTPException(status_code=404, detail="Customer Not Found")
    return customer


@router.put("/{customer_id}", response_model=CustomerResponse)
def update_customer(customer_id: int, customer: CustomerRequestBody, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    customer = customer_crud.update(customer_id, customer, db)
    if not customer:
        raise HTTPException(status_code=404, detail="Customer Not Found")
    return customer


@router.delete("/{customer_id}")
def delete_customer(customer_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    customer = customer_crud.delete(customer_id, db)
    if not customer:
        raise HTTPException(status_code=404, detail="Customer Not Found")
    return {"message": f"Customer with id: {customer_id} deleted"}
