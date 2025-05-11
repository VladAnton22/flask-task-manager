from app import db
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Date, ForeignKey, Integer
from datetime import date
from flask_login import UserMixin
from typing import List

#------Users table------
class User(db.Model, UserMixin):
    __tablename__ = "user_account"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    password_hash: Mapped[str] = mapped_column(nullable=False)

    tasks: Mapped[List["Task"]] = relationship(back_populates="user")

    def set_password(self, password: str):
        from werkzeug.security import generate_password_hash
        self.password_hash = generate_password_hash(password)

    def check_password(self, password: str) -> bool:
        from werkzeug.security import check_password_hash
        return check_password_hash(self.password_hash, password)
    
    def __repr__(self):
        return f'User(id={self.id!r}, name={self.name!r})'
    
#------Tasks table------
class Task(db.Model):
    __tablename__ = "task"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(40))
    description: Mapped[str] = mapped_column(String(255), nullable=True)
    due_date: Mapped[date] = mapped_column(Date, nullable=True)
    priority: Mapped[int] = mapped_column(Integer, nullable=False)
    status: Mapped[str] = mapped_column(String(15))
    user_id: Mapped[int] = mapped_column(ForeignKey("user_account.id"), nullable=False)  

    user: Mapped["User"] = relationship(back_populates="tasks")

    def __repr__(self):
        return f'Task(id={self.id!r}, title={self.title!r}, description={self.description!r}, due_date={self.due_date!r}, priority={self.priority!r}, status={self.status!r})'
