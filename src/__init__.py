from fastapi import FastAPI
from src.books.routes import book_router

version = "v1"
# creating app instance
app = FastAPI(
    title="Book API",
    description="A simple API to manage books",
    version=version
)

app.include_router(book_router, prefix=f"/api/{version}/books", tags=["books"])