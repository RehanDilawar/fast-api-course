from fastapi import FastAPI, Body
from pydantic import BaseModel
app = FastAPI()

class Book:
  id: int
  title: str
  author: str
  description: str
  rating: int

  def __init__(self, id: int, title: str, author: str, description: str, rating: int):
    self.id = id
    self.title = title
    self.author = author
    self.description = description
    self.rating = rating
class BookRequest(BaseModel):
    id: int
    title: str
    author: str
    description: str
    rating: int
BOOKS = [
  Book(1, "A Tale of Two Cities", "Charles Dickens", "A historical novel by Charles Dickens, first published in 1859. It tells the story of the French Revolution.", 5),
  Book(2, "Oliver Twist", "Charles Dickens", "A historical novel by Charles Dickens, first published in 1838. It tells the story of an orphan boy named Oliver Twist who endures a difficult childhood in the streets of London.", 4),
  Book(3, "Great Expectations", "Charles Dickens", "A historical novel by Charles Dickens, first published in 1861. It tells the story of an orphan boy named Pip who rises from humble beginnings to become a gentleman.", 5),
  Book(4, "Book 4", "Author 4", "Description 4", 2),
  Book(5, "Book 5", "Author 5", "Description 5", 1),
  Book(6, "Book 6", "Author 6", "Description 6", 3)
]

@app.get("/books")
async def read_all_books():
    return BOOKS

@app.post("/create-book")
async def create_book(book_request: BookRequest):
  new_book = Book(**book_request.dict())
  BOOKS.append(new_book)