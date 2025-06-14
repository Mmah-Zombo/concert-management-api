from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from schemas.user import UserCreate, UserOut, UserExit, Token
from models.user import User
from utils.auth import hash_password, verify_password, create_access_token
from datetime import datetime
from dependencies.auth import  get_current_user

router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post("/register", response_model=UserOut)
def register(user: UserCreate, db: Session = Depends(get_db)):
    # Check if username already exists
    if db.query(User).filter(User.username == user.username).first():
        raise HTTPException(status_code=400, detail="Username already registered")

    hashed_pw = hash_password(user.password)
    db_user = User(
        username=user.username,
        password=hashed_pw,
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


@router.post("/login", response_model=Token)
def login(user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.username == user.username).first()
    if not db_user:
        raise HTTPException(status_code=400, detail="User Not Found")

    if not verify_password(user.password, db_user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    access_token = create_access_token(data={"sub": db_user.username})
    return {"access_token": access_token, "token_type": "bearer"}


@router.post("/logout", response_model=UserExit)
def logout(user: User = Depends(get_current_user)):
    return user


@router.post("/delete", response_model=UserExit)
def delete(user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    db.delete(user)
    db.commit()
    return user
