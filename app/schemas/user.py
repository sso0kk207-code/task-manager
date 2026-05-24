from pydantic import BaseModel, EmailStr, Field, ConfigDict
from uuid import UUID
from datetime import date
from typing import Optional

class UserBase(BaseModel):
    email: EmailStr
    first_name: str = Field(min_length=1, max_length=50)
    last_name: str = Field(min_length=1, max_length=50)
    date_of_birth: date


class UserCreate(UserBase):
    password: str = Field(min_length=8, repr=False)


class UserUpdate(BaseModel):
    email: Optional[EmailStr] = None
    first_name: Optional[str] = Field(None, min_length=1, max_length=50)
    last_name: Optional[str] = Field(None, min_length=1, max_length=50)
    date_of_birth: Optional[date] = None


class UserResponse(UserBase):
    id: UUID
    
    model_config = ConfigDict(from_attributes=True)