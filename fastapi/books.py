from fastapi import FastAPI

app = FastAPI()

BOOKS = BOOKS = [
    {"title": "Book 1", "author": "Author 1", "year": 2020, "genre": "Fiction", "language": "English"},
    {"title": "Book 2", "author": "Author 2", "year": 2018, "genre": "Non-Fiction", "language": "English"},
    {"title": "Book 3", "author": "Author 3", "year": 2021, "genre": "Science Fiction", "language": "English"},
    {"title": "Book 4", "author": "Author 4", "year": 2019, "genre": "Fantasy", "language": "English"},
    {"title": "Book 5", "author": "Author 5", "year": 2022, "genre": "Mystery", "language": "English"},
    {"title": "Book 6", "author": "Author 6", "year": 2017, "genre": "History", "language": "Spanish"},
    {"title": "Book 7", "author": "Author 7", "year": 2016, "genre": "History", "language": "Spanish"},
    {"title": "Book 8", "author": "Author 8", "year": 2023, "genre": "Romance", "language": "Spanish"},
    {"title": "Book 9", "author": "Author 9", "year": 2015, "genre": "Horror", "language": "Spanish"},
    {"title": "Book 10", "author": "Author 10", "year": 2014, "genre": "Self-Help", "language": "Spanish"},
    {"title": "Book 11", "author": "Author 11", "year": 2023, "genre": "Thriller", "language": "Spanish"}
]


@app.get("/")
async def welcome():
    return {"message": "Hello, Sahil kumar!"}


@app.get("/books")
async def get_books():
    return BOOKS


@app.get("/books/{book_genre}")  # Dynamic Path Parameter example.
async def get_book(book_genre: str):
    books = [book for book in BOOKS if book["genre"].casefold() == book_genre.casefold()]
    return books


# Path and Query Parameter both together example. Example URL -> /books/english?limit=2&skip=2
@app.get("/books/lang/{book_language}")
async def get_book(book_language: str, limit: int = 10, skip: int = 0):
    books = [book for book in BOOKS if book["language"].casefold() == book_language.casefold()]
    return books[skip: skip + limit]
