from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Boolean, Text
from sqlalchemy.orm import relationship

from db_conf import Base

class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(Text, index=True)
    year_published = Column(Integer, index=True)
    pages = Column(Integer, index=True)
    is_fiction = Column(Boolean, default=True)
    author_name = Column(String, ForeignKey("authors.name"))

    author = relationship("Author", back_populates="books")

class Author(Base):
    __tablename__ = "authors"
    name = Column(String, primary_key=True, index=True)
    age = Column(Integer, index=True)
    born = Column(Integer, index=True)

    books = relationship("Book", back_populates="author")
