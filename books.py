from fastapi import FastAPI, Body

app = FastAPI()

BOOKS = [
    {"title": "Book 1", "author": "Author 1", "category": "Science"},
    {"title": "Book 2", "author": "Author 2", "category": "History"},
    {"title": "Book 3", "author": "Author 3", "category": "Math"},
    {"title": "Book 4", "author": "Author 4", "category": "Fantasy"},
    {"title": "Book 5", "author": "Author 5", "category": "Math"},
    {"title": "Book 6", "author": "Author 1", "category": "History"},
    {"title": "Book 7", "author": "Author 7", "category": "Poetry"},
    {"title": "Book 8", "author": "Author 8", "category": "Religion"},
]

@app.get("/books")
async def read_all_books():
    return BOOKS

@app.get("/books/{book_title}")
async def read_all_books(book_title: str):
    for book in BOOKS:
        if book.get("title").casefold() == book_title.casefold():
            return book
    return {"error": "Book not found"}

@app.get("/books/")
async def read_category_by_query(category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get("category").casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return

@app.get("/books/by-author/")
async def read_author_by_query(author: str):
    books_to_return = []
    for book in BOOKS:
        if book.get("author").casefold() == author.casefold():
            books_to_return.append(book)
    return books_to_return
'''Order matters a ton in fastAPI, always make sure API with less specific path parameters are defined first'''
@app.get("/books/{book_author}/")
async def read_author_by_query(book_author: str, category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get("author").casefold() == book_author.casefold() and \
            book.get("category").casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return

@app.post("/books/create-book")
async def create_book(new_book=Body()):
    BOOKS.append(new_book)

@app.put("/books/update-book")
async def update_book(updated_book=Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get("title") == updated_book.get("title"):
            BOOKS[i] = updated_book
            break

@app.delete("/books/delete-book/{book_title}")
async def delete_book(book_title: str):
    for i in range(len(BOOKS)):
        if BOOKS[i].get("title").casefold() == book_title.casefold():
            BOOKS.pop(i)
            break