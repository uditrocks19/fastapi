
from fastapi import APIRouter, status
from typing import List
from fastapi.exceptions import HTTPException
from src.books.book_data import books
from src.books.schemas import Book, BookUpdate

book_router = APIRouter()

@book_router.get('/', response_model=List[Book])
async def get_all_books() ->List[dict]:
    return books

@book_router.post('/', status_code=status.HTTP_201_CREATED)
async def create_a_book(book_data:Book) -> dict:
    new_book = book_data.model_dump()
    books.append(new_book)
    return new_book

@book_router.get('/{book_id}')
async def get_book(book_id: int) -> dict:
    for book in books:
        if book["id"] == book_id:
            return book 
    
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Book with {book_id} not found"
        )

@book_router.patch('/{book_id}')
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


@book_router.delete('/{book_id}')
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
