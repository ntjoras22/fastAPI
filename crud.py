from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

# Use plural name for the list of books to avoid confusion with the model
books = [
    {
        "id": 1,
        "title": "The alchemist",
        "author": "Paulo Coelho",
        "price": 10.99
    },
    {
        "id": 2,
        "title": "The secret",
        "author": "Rhonda Byrne",
        "price": 12.99
    },
    {
        "id": 3,
        "title": "The monk who sold his Ferrari",
        "author": "Robin Sharma",
        "price": 15.99
    },
    {
        "id": 4,
        "title": "The secret",
        "author": "Rhonda Byrne",
        "price": 12.99  
    },
]

app = FastAPI()

# Use CapCase for the model name (PEP 8)
class Book(BaseModel):
    id: int
    title: str
    author: str
    price: float    

@app.get("/book")
def get_books():
    return books


@app.get("/book/{book_id}")
def get_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
         return book 
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Book not found")



@app.post("/book")
def create_book(book: Book):
    # Convert Pydantic model to dictionary
    new_book_dict = book.model_dump()
    # Append to the GLOBAL books list
    books.append(new_book_dict)
    # Return the dictionary (FastAPI will serialize it to JSON)
    return new_book_dict

class BookUpdate(BaseModel):
    title: str
    author: str
    price: float

@app.put("/book/{book_id}")
def update_book(book_id: int, updated_book_data: BookUpdate):
    for existing_book in books:
        if existing_book["id"] == book_id:
            existing_book["title"] = updated_book_data.title
            existing_book["author"] = updated_book_data.author
            existing_book["price"] = updated_book_data.price
            return existing_book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")

@app.delete("/book/{book_id}")
def delete_book(book_id:int):
    for book in books:
        if book["id"] == book_id:
            books.remove(book)
            return {"message": "Book deleted successfully"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found") 