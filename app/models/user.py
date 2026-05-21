from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, Mapped
from app.core.db import Base, str_uniq, int_pk, str_null_true
from datetime import date


class User(Base):
    id: Mapped[int_pk]
    email: Mapped[str_uniq]
    hashed_password: Mapped[str]
    first_name: Mapped[str]
    second_name: Mapped[str_null_true]
    email: Mapped[str_uniq]
    date_of_birth: Mapped[date]
    is_active: Mapped[bool]
    
    def __str__(self) -> str_uniq:
        return (f"User-{self.id}: {self.first_name}\nEmail: {self.email}")
