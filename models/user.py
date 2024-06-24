from typing import Optional
from datetime import date
from app import db, ma
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String

class User(db.Model):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(String(100))
    last_name: Mapped[str] = mapped_column(String(100))
    email: Mapped[str] = mapped_column(String(100))
    password: Mapped[str] = mapped_column(String(100))
    date_created: Mapped[date] = date.today()
    last_login: Mapped[date] =  date.today()                               #how to figure out custom date?

    subscriptions: Mapped["Subscription"] = relationship(back_populates='user')
    tickets: Mapped["Ticket"] = relationship(back_populates='user')

class UserSchema(ma.Schema):
    class Meta:
        fields = ("id", "first_name", "last_name", "email", "password", "date_created", "last_login")