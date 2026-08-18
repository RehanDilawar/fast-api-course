from fastapi import FastAPI, Path, Query
from pydantic import BaseModel, Field
from typing import Optional
app = FastAPI()

class Book:
  id: int
  title: str
  author: str
  description: str
  rating: int
  published_date: int

  def __init__(self, id: int, title: str, author: str, description: str, rating: int, published_date: int):
    self.id = id
    self.title = title
    self.author = author
    self.description = description
    self.rating = rating
    self.published_date = published_date
class BookRequest(BaseModel):
    id: Optional[int] = Field(description="The ID is not needed on create", default=None)
    title: str = Field(min_length=3)
    author: str = Field(min_length=3)
    description: str = Field(min_length=3, max_length=100)
    rating: int = Field(ge=0, le=5)
    published_date: int = Field(ge=1800, le=2026)

    model_config = {
      "json_schema_extra": {
        "example": {
          "title": "Title of the book",
          "author": "Author of the book",
          "description": "Description of the book",
          "rating": 5,
          "published_date": 2022
        }
      }
    }
BOOKS = [
  Book(1, "A Tale of Two Cities", "Charles Dickens", "A historical novel by Charles Dickens, first published in 1859. It tells the story of the French Revolution.", 5, 1859),
  Book(2, "Oliver Twist", "Charles Dickens", "A historical novel by Charles Dickens, first published in 1838. It tells the story of an orphan boy named Oliver Twist who endures a difficult childhood in the streets of London.", 4, 1838),
  Book(3, "Great Expectations", "Charles Dickens", "A historical novel by Charles Dickens, first published in 1861. It tells the story of an orphan boy named Pip who rises from humble beginnings to become a gentleman.", 5, 1861),
  Book(4, "Book 4", "Author 4", "Description 4", 2, 2022),
  Book(5, "Book 5", "Author 5", "Description 5", 1, 2022),
  Book(6, "Book 6", "Author 6", "Description 6", 3, 2022)
]

@app.get("/books")
async def read_all_books():
    return BOOKS

@app.get("/books/{book_id}")
async def read_book(book_id: int = Path(gt=0)):
    for book in BOOKS:
        if book.id == book_id:
            return book
    return {"error": "Book not found"}

@app.get("/books/")
async def read_book_by_rating(rating: int = Query(ge=0, le=5)):
  books_to_return = []
  for book in BOOKS:
    if book.rating == rating:
      books_to_return.append(book)
  return books_to_return

@app.get("/books/published/")
async def read_book_by_published_date(published_date: int = Query(ge=1800, le=2026)):
  books_to_return = []
  for book in BOOKS:
    if book.published_date == published_date:
      books_to_return.append(book)
  return books_to_return

@app.post("/create-book")
async def create_book(book_request: BookRequest):
  new_book = Book(**book_request.dict())
  BOOKS.append(find_book_id(new_book))

def find_book_id(book: Book):

  book.id = 1 if len(BOOKS) == 0 else BOOKS[-1].id + 1


  # if len(BOOKS) > 0:
  #   book.id = BOOKS[-1].id + 1
  # else:
  #   book.id = 1
  return book


@app.put("/books/update_book")
async def update_book(book: BookRequest):
  for i in range(len(BOOKS)):
    if BOOKS[i].id == book.id:
      BOOKS[i] = book


@app.delete("/books/{book_id}")
async def delete_book(book_id: int = Path(gt=0)):
  for i in range(len(BOOKS)):
    if BOOKS[i].id == book_id:
      BOOKS.pop(i)
      return {"message": "Book deleted successfully"}