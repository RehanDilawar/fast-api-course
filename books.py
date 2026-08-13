from fastapi import FastAPI

app = FastAPI()

BOOKS = [
    {'title': 'Book 1', 'author': 'Author 1', 'category': 'Science'},
    {'title': 'Book 2', 'author': 'Author 2', 'category': 'History'},
    {'title': 'Book 3', 'author': 'Author 3', 'category': 'Math'},
    {'title': 'Book 4', 'author': 'Author 4', 'category': 'Fantasy'},
    {'title': 'Book 5', 'author': 'Author 5', 'category': 'Math'},
    {'title': 'Book 6', 'author': 'Author 1', 'category': 'History'},
    {'title': 'Book 7', 'author': 'Author 7', 'category': 'Poetry'},
    {'title': 'Book 8', 'author': 'Author 8', 'category': 'Religion'},
]

@app.get("/books")
async def read_all_books():
    return BOOKS

@app.get("/books/{book_title}")
async def read_all_books(book_title: str):
    for book in BOOKS:
        if book.get('title').casefold() == book_title.casefold():
            return book
    return {'error': 'Book not found'}

@app.get("/books/")
async def read_category_by_query(category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('category').casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return

@app.get("/books/{book_author}/")
async def read_author_by_query(book_author: str, category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('author').casefold() == book_author.casefold() and \
            book.get('category').casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return