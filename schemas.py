from datetime import date
from typing import List

from pydantic import BaseModel

from db.models import Book


class AuthorBase(BaseModel):
    name: str
    bio: str
    books: List[Book]


class Author(AuthorBase):
    id: int

    class Config:
        orm_mode = True


class AuthorCreate(AuthorBase):
    pass


class BookBase(BaseModel):
    title: str
    summary: str
    publication_date: date
    author_id: int


class Book(BookBase):
    id: int

    class Config:
        orm_mode = True


class BookCreate(BookBase):
    pass
