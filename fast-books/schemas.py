from pydantic import BaseModel
from typing import Union, List


class BookBase(BaseModel):
    title: str
    description: Union[str, None] = None
    year_published: int
    pages: int
    is_fiction: bool
    author_name: str

class BookCreate(BookBase):
    pass

class Book(BookBase):

    class Config:
        orm_mode: True


class AuthorBase(BaseModel):
    name: str
    age: int
    born: int

class AuthorCreate(AuthorBase):
    pass
    
class Author(BookBase):
    books: List[Book] = []

    class Config:
        orm_mode: True

