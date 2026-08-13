from fastapi import FastAPI

app = FastAPI()

BOOKS = [
    {'title': 'The Great Gatsby', 'author': 'F. Scott Fitzgerald', 'category': 'Classic'},
    {'title': 'To Kill a Mockingbird', 'author': 'Harper Lee', 'category': 'Classic'},
    {'title': '1984', 'author': 'George Orwell', 'category': 'Classic'},
    {'title': 'The Catcher in the Rye', 'author': 'J.D. Salinger', 'category': 'Classic'},
    {'title': 'The Great Gatsby', 'author': 'F. Scott Fitzgerald', 'category': 'Classic'},
    {'title': 'To Kill a Mockingbird', 'author': 'Harper Lee', 'category': 'Classic'},
    {'title': '1984', 'author': 'George Orwell', 'category': 'Classic'},
    {'title': 'The Catcher in the Rye', 'author': 'J.D. Salinger', 'category': 'Classic'},
]

@app.get("/books")
async def read_all_books():
    return BOOKS
