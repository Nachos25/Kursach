from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from ..database import get_db
from ..models import User
from ..schemas import UserCreate, UserPublic, Token, MeResponse
from ..security import get_password_hash, verify_password, create_access_token
from ..security import get_current_user

router = APIRouter(prefix="/api/auth", tags=["auth"])


@router.post("/register", response_model=UserPublic)
def register(user_in: UserCreate, db: Session = Depends(get_db)):
    existing = db.query(User).filter(User.username == user_in.username).first()
    if existing:
        raise HTTPException(status_code=400, detail="Логін вже використовується")
    user = User(
        username=user_in.username,
        email=user_in.email or f"{user_in.username}@local",
        password_hash=get_password_hash(user_in.password),
        full_name=user_in.full_name,
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


@router.post("/login", response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == form_data.username).first()
    if not user or not verify_password(form_data.password, user.password_hash):
        raise HTTPException(status_code=400, detail="Невірні дані для входу")
    token = create_access_token(subject=user.username)
    return {"access_token": token, "token_type": "bearer"}


@router.get("/me", response_model=MeResponse)
def me(current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    orders = db.query(User).get(current_user.id).orders  # lazy load items
    return {"user": current_user, "orders": orders}


@router.post("/instant", response_model=Token)
def instant(username: str, password: str | None = None, full_name: str | None = None, db: Session = Depends(get_db)):
    """
    Спрощена реєстрація: створює користувача якщо його немає і одразу повертає токен.
    """
    user = db.query(User).filter(User.username == username).first()
    if not user:
        user = User(
            username=username,
            email=f"{username}@local",
            password_hash=get_password_hash(password or "password"),
            full_name=full_name,
        )
        db.add(user)
        db.commit()
        db.refresh(user)
    token = create_access_token(subject=user.username)
    return {"access_token": token, "token_type": "bearer"}




