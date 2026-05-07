from datetime import date
from typing import List

from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Mapped, relationship

Base = declarative_base()

class Author(Base):
    __tablename__ = "author"

    id: int = Column(Integer, primary_key=True)
    name: str = Column(String(255), unique=True)
    bio: str = Column(String(5000))
    books: Mapped[List["Book"]] = relationship(back_populates="author")


class Book(Base):
    __tablename__ = "book"

    id: int = Column(Integer, primary_key=True)
    title: str = Column(String(255))
    summary: str = Column(String(2000))
    publication_date: date = Column(Date)
    author_id: int = Column(Integer, ForeignKey("author.id"))

    author = relationship("Author", back_populates="books")
