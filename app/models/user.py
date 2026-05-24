from sqlalchemy.orm import Mapped
from app.core.db import Base, str_uniq, str_null_true
from datetime import date


class User(Base):
    email: Mapped[str_uniq]
    hashed_password: Mapped[str]
    first_name: Mapped[str]
    last_name: Mapped[str_null_true]
    date_of_birth: Mapped[date]
    is_active: Mapped[bool] = False

    def __repr__(self) -> str:
        return f"User(id={self.id}, email={self.email})"