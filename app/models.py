from app import db
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer
from flask_login import UserMixin

#------Users table------
class User(db.Model, UserMixin):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    password_hash: Mapped[str] = mapped_column(nullable=False)

    def set_password(self, password: str):
        from werkzeug.security import generate_password_hash
        self.password_hash = generate_password_hash(password)

    def check_password(self, password: str) -> bool:
        from werkzeug.security import check_password_hash
        return check_password_hash(self.password_hash, password)
    
    def __repr__(self):
        return f'User(id={self.id!r}, name={self.name!r})'