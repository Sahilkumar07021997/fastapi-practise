from typing import Optional

from fastapi import FastAPI, Path, Query
from pydantic import BaseModel, Field

app = FastAPI()


class Book:
    id: int
    title: str
    author: str
    description: str
    rating: str

    def __init__(self, id: int, title: str, author: str, description: str, rating: str):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating


class BookRequest(BaseModel):
    id: Optional[int] = Field(description='ID is not needed on create', default=None)
    title: str = Field(min_length=3, max_length=100)
    author: str = Field(min_length=1, max_length=50)
    description: str = Field(min_length=1, max_length=100)
    rating: int = Field(gt=-1, lt=5)

    model_config = {
        "json_schema_extra": {
            "example": {
                "title": "New Book",
                "author": "New Author",
                "description": "New Description",
                "rating": "5"
            }
        }
    }


BOOKS = [
    Book(1, "Book 1", "Author 1", "Description 1", "4"),
    Book(2, "Book 2", "Author 2", "Description 2", "4"),
    Book(3, "Book 3", "Author 3", "Description 3", "3"),
    Book(4, "Book 4", "Author 4", "Description 4", "5"),
    Book(5, "Book 5", "Author 5", "Description 5", "2"),
    Book(6, "Book 6", "Author 6", "Description 6", "1"),
    Book(7, "Book 7", "Author 7", "Description 7", "5"),
    Book(8, "Book 8", "Author 8", "Description 8", "3"),
    Book(9, "Book 9", "Author 9", "Description 9", "4"),
    Book(10, "Book 10", "Author 10", "Description 10", "2"),
]


@app.get("/books")
async def read_all_books():
    return BOOKS


# @app.post("/create_book")  # Before Validation
# async def create_book(new_book=Body(...)):
#     BOOKS.append(new_book)
#     return BOOKS[-1]

@app.post("/create_book")  # After adding Validation
async def create_book(new_book: BookRequest):
    book = Book(**new_book.model_dump())
    BOOKS.append(get_book_index(book))
    return BOOKS[-1]


def get_book_index(book: Book):
    book.id = 1 if len(BOOKS) == 0 else BOOKS[-1].id + 1
    return book


@app.get("/books/{book_id}")  # Path Parameter with Validation example.
async def read_book(book_id: int = Path(..., gt=0, description="The ID of the user")):
    for book in BOOKS:
        if book.id == book_id:
            return book
    return {"message": "Book not found"}


@app.get("/books/")  # Query Parameter example wth Query validation. Example URL -> /books/?book_rating=4
async def read_book_by_rating(book_rating: int = Query(..., gt=-1, lt=6, description="The rating of the book")):
    books = [book for book in BOOKS if book.rating == str(book_rating)]
    return books


@app.put("/books/update_book")
async def update_book(updated_book: BookRequest):
    for index, book in enumerate(BOOKS):
        if book.id == updated_book.id:
            BOOKS[index] = Book(**updated_book.model_dump())
            return BOOKS[index]
    return {"message": "Book not found"}


@app.delete("/books/{book_id}")
async def delete_book(book_id: int):
    for index, book in enumerate(BOOKS):
        if book.id == book_id:
            deleted_book = BOOKS.pop(index)
            return {"message": "Book deleted successfully", "book": deleted_book}
    return {"message": "Book not found"}
