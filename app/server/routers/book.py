from fastapi import APIRouter, Body, Request
from fastapi.encoders import jsonable_encoder
import requests 
from ..models.book import BookSchema, UpdateBookModel
from ..models.user import (
    ErrorResponseModel,
    ResponseModel,
)

from ..database import (
    add_book,
    delete_book,
    retrieve_book,
    retrieve_books,
    update_book,
)


router = APIRouter()

@router.get("/search/{booksearch}")
async def book_api_data(request: Request, booksearch):
    url = f'https://www.googleapis.com/books/v1/volumes?q={booksearch}'
    r = requests.get(url).json()
    print(r)
    return ResponseModel(r, "Results with matching titles")
    # return {"message": "Search worked"}

# Create a new book
@router.post("/", response_description="Book successfully created")
async def add_book_data(book: BookSchema = Body(...)):
    book = jsonable_encoder(book)
    new_book = await add_book(book)
    return ResponseModel(new_book, "Book added successfully")

# Shows all books
@router.get("/", response_description="All books retrieved")
async def get_books():
    books = await retrieve_books()
    if books:
        return ResponseModel(books, "Book data successfully retrieved")
    return ResponseModel(books, "Empty list returned")

# Get single book based on ID
@router.get("/{id}", response_description="Book data successfully retrieved")
async def get_single_book(id):
    if len(id) != 24:
        return ErrorResponseModel("An error occurred", 404, "id length must be a 24-character hex string")
    else:
        book = await retrieve_book(id)
        if book:
            return ResponseModel(book, "Book data retrieved successfully")
        return ErrorResponseModel("An error occurred.", 404, "Book doesn't exist.")

# Update a book based on ID
@router.put("/{id}")
async def update_book_data(id: str, req: UpdateBookModel = Body(...)):
    if len(id) != 24:
        return ErrorResponseModel("An error occurred", 404, "id length must be a 24-character hex string")
    else:
        req = {k: v for k, v in req.dict().items() if v is not None}
        updated_book = await update_book(id, req)
        if updated_book:
            return {"message": "Book with ID: {} has been updated successfully".format(id)}
        return ErrorResponseModel(
            "An error occurred",
            404,
            "There was an error updating the book data",
        )

# Destroy a book based on ID
@router.delete("/{id}", response_description="Book data deleted from the database")
async def delete_book_data(id: str):
    if len(id) != 24:
        return ErrorResponseModel("An error occurred", 404, "id length must be a 24-character hex string")
    else:
        deleted_book = await delete_book(id)
        if deleted_book:
            return {"message": "Book with ID: {} has been removed successfully".format(id)}
        return ErrorResponseModel(
            "An error occurred", 404, "Book with id {} doesn't exist".format(id)
        )