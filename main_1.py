from fastapi import FastAPI, status
from fastapi.exceptions import HTTPException
from pydantic import BaseModel
from typing import Optional, List

app = FastAPI()

books = [
    {"id": 1, "author": "George Orwell", "book_name": "1984", "genre": "Dystopian"},
    {"id": 2, "author": "Jane Austen", "book_name": "Pride and Prejudice", "genre": "Romance"},
    {"id": 3, "author": "J.K. Rowling", "book_name": "Harry Potter and the Sorcerer's Stone", "genre": "Fantasy"},
    {"id": 4, "author": "F. Scott Fitzgerald", "book_name": "The Great Gatsby", "genre": "Classic"},
    {"id": 5, "author": "Harper Lee", "book_name": "To Kill a Mockingbird", "genre": "Classic"},
    {"id": 6, "author": "Agatha Christie", "book_name": "Murder on the Orient Express", "genre": "Mystery"},
    {"id": 7, "author": "J.R.R. Tolkien", "book_name": "The Hobbit", "genre": "Fantasy"},
    {"id": 8, "author": "Mark Twain", "book_name": "The Adventures of Tom Sawyer", "genre": "Adventure"},
    {"id": 9, "author": "Mary Shelley", "book_name": "Frankenstein", "genre": "Horror"},
    {"id": 10, "author": "Ernest Hemingway", "book_name": "The Old Man and the Sea", "genre": "Classic"}
]

class Book(BaseModel):
    id: int
    author: str
    book_name: str
    genre: str

class BookUpdate(BaseModel):
    author: str
    book_name: str
    genre: str

@app.get('/books', response_model=List[Book])
async def get_all_books() ->List[dict]:
    return books

@app.post('/books', status_code=status.HTTP_201_CREATED)
async def create_a_book(book_data:Book) -> dict:
    new_book = book_data.model_dump()
    books.append(new_book)
    return new_book

@app.get('/books/{book_id}')
async def get_book(book_id: int) -> dict:
    for book in books:
        if book["id"] == book_id:
            return book 
    
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Book with {book_id} not found"
        )

@app.patch('/books/{book_id}')
async def delete_book(book_id: int, book_update_data:BookUpdate) -> dict:
    book_update = book_update_data.model_dump()
    for book in books:
        if book["id"] == book_id:
            book["author"] = book_update["author"]
            book["book_name"] = book_update["book_name"]
            book["genre"] = book_update["genre"]
            return {"message" : f"Book with {book_id} updated",
                    "book": book
            }
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"Book with id: {book_id} not found"
                        )


@app.delete('/books/{book_id}')
async def delete_book(book_id: int):
    deleted_book = None
    for i, book in enumerate(books):
        if book["id"] == book_id:
            deleted_book = books.pop(i)
            return {
                "message" : f"Book with id : {book_id} deleted",
                "details" : deleted_book
                }
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
          detail=f"book with id {book_id} not found"
        )
