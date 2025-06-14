from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi import Depends, HTTPException
from utils.auth import decode_access_token
from database import get_db
from models.user import User
from sqlalchemy.orm import Session

auth_scheme = HTTPBearer()


def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(auth_scheme),
    db: Session = Depends(get_db)
):
    token = credentials.credentials
    payload = decode_access_token(token)
    if not payload:
        raise HTTPException(status_code=401, detail="Invalid token")

    user = db.query(User).filter(User.username == payload.get("sub")).first()
    if not user:
        raise HTTPException(status_code=401, detail="User not found")
    return user
