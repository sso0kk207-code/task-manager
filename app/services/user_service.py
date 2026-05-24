from app.models.user import User
from pydantic import EmailStr
from app.core.security import verify_password
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

async def get_user_by_email(user_email: EmailStr, db: AsyncSession) -> User | None:
    query = select(User).where(User.email == user_email)
    result = await db.execute(query)
    return result.scalar_one_or_none()

async def authenticate_user(user_email: EmailStr, password: str, db: AsyncSession) -> User | None:
    user = await get_user_by_email(user_email, db)
    if not user:
        return None
    if not verify_password(password, user.hashed_password):
        return None
    return user