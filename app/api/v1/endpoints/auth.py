from fastapi import APIRouter, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.db import get_db
from app.schemas.token import Token
from app.schemas.user import UserCreate
from app.models.user import User
from app.services.user_service import authenticate_user
from app.core.security import create_access_token, get_password_hash
from app.services.user_service import get_user_by_email

router = APIRouter(prefix="/auth", tags=["authentication"])

@router.post("/register", response_model=Token)
async def register(
    user_in: UserCreate,
    db: AsyncSession = Depends(get_db)
    ):
    res = await get_user_by_email(user_in.email, db)
    if res is not None:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="User with the same email already exists",
            headers={"WWW-Authenticate": "Bearer"}
        )
    hashed_pwd = get_password_hash(user_in.password)
    db_user = User(
        **user_in.model_dump(exclude={"password"}),
        hashed_password=hashed_pwd
    )
    access_token = create_access_token(data={"sub": db_user.email})
    db.add(db_user)
    await db.commit()
    return Token(access_token=access_token, token_type="bearer")

@router.post("/login", response_model=Token)
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: AsyncSession = Depends(get_db)
    ):
    user = await authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"}
        )
    
    access_token = create_access_token(data={"sub": user.email})
    return Token(access_token=access_token, token_type="bearer")