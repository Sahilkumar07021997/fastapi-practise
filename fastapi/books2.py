from fastapi import FastAPI
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
    id: int
    title: str = Field(min_length=3, max_length=100)
    author: str = Field(min_length=1, max_length=50)
    description: str = Field(min_length=1, max_length=100)
    rating: float = Field(gt=-1, lt=5.0)


BOOKS = [
    Book(1, "Book 1", "Author 1", "Description 1", "4.5"),
    Book(2, "Book 2", "Author 2", "Description 2", "4.0"),
    Book(3, "Book 3", "Author 3", "Description 3", "3.5"),
    Book(4, "Book 4", "Author 4", "Description 4", "5.0"),
    Book(5, "Book 5", "Author 5", "Description 5", "4.8"),
    Book(6, "Book 6", "Author 6", "Description 6", "4.2"),
    Book(7, "Book 7", "Author 7", "Description 7", "3.8"),
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
