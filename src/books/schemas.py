from pydantic import BaseModel

class Book(BaseModel):
    id: int
    author: str
    book_name: str
    genre: str

class BookUpdate(BaseModel):
    author: str
    book_name: str
    genre: str

