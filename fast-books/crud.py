from sqlalchemy.orm import Session
import models, schemas


def add_book(db: Session, book: schemas.BookCreate):
    db_book = models.Book(**book.dict())

    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

def add_author(db: Session, author: schemas.AuthorCreate):
    db_author = models.Author(**author.dict())
    db.add(db_author)
    db.commit()
    db.refresh(db_author)
    return db_author

def get_all_books(db: Session):
    return db.query(models.Book).all()

def get_book_by_title(db: Session, title: str):
    return db.query(models.Book).filter(models.Book.title == title).first()

def get_author_by_name(db: Session, name: str):
    return db.query(models.Author).filter(models.Author.name == name).first()

