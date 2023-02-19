import uvicorn
import os
from typing import List
import models, schemas, crud
from fastapi import FastAPI, Depends, HTTPException, Request, Response
from fastapi_sqlalchemy import DBSessionMiddleware
from sqlalchemy.orm import Session
from dotenv import load_dotenv
from db_conf import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

load_dotenv(".env")

app.add_middleware(DBSessionMiddleware, db_url=os.environ["DATABASE_URL"])

#@app.middleware("http")
#async def db_session_middleware(request: Request, call_next):
#    response = Response("Internal server error", status_code=500)
#    try:
#        request.state.db = SessionLocal()
#        response = await call_next(request)
#    finally:
#        request.state.db.close()
#    return response

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#middlseware session
#def get_db(request: Request):
#    return request.state.db


@app.get('/')
async def root():
    return {"message": "Hello"}


@app.post('/add-book/', response_model=schemas.Book)
def add_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    db_book = crud.get_book_by_title(db, title=book.title)
    if db_book:
        raise HTTPException(status_code=400, detail="Book already exists in database.")
    return crud.add_book(db=db, book=book)

@app.post('/add-author/', response_model=schemas.Author)
def add_author(author: schemas.AuthorCreate, db: Session = Depends(get_db)):
    db_author = crud.get_author_by_name(db, name=author.name)
    if db_author:
        raise HTTPException(status_code=400, detail="Author already exists in database.")
    return crud.add_author(db=db, author=author)


@app.get('/books/') #response_model=List[schemas.Book])
def get_books(db: Session = Depends(get_db)):
    books = crud.get_all_books(db)
    return books


