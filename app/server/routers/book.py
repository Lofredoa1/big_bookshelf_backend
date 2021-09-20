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
    delete_user,
    retrieve_user,
    retrieve_users,
    update_user,
)


router = APIRouter()

@router.get("/search/{booksearch}")
async def book_api_data(request: Request, booksearch):
    url = f'https://www.googleapis.com/books/v1/volumes?q={booksearch}'
    r = requests.get(url).json()
    return r

##
@router.post("/")
async def add_book_data(book: BookSchema = Body(...)):
    book = jsonable_encoder(book)
    new_book = await add_book(book)
    return ResponseModel(new_book, "Book added successfully.")


# @router.get("/", response_description="Students retrieved")
# async def get_students():
#     students = await retrieve_students()
#     if students:
#         return ResponseModel(students, "Students data retrieved successfully")
#     return ResponseModel(students, "Empty list returned")


# @router.get("/{id}", response_description="Student data retrieved")
# async def get_student_data(id):
#     if len(id) != 24:
#         return ErrorResponseModel("An error occurred", 404, "id length must be a 24-character hex string"        )
#     else:
#         student = await retrieve_student(id)
#         if student:
#             return ResponseModel(student, "Student data retrieved successfully")
#         return ErrorResponseModel("An error occurred.", 404, "Student doesn't exist.")

# @router.put("/{id}")
# async def update_student_data(id: str, req: UpdateStudentModel = Body(...)):
#     if len(id) != 24:
#         return ErrorResponseModel("An error occurred", 404, "id length must be a 24-character hex string"        )
#     else:
#         req = {k: v for k, v in req.dict().items() if v is not None}
#         updated_student = await update_student(id, req)
#         if updated_student:
#             return ResponseModel(
#                 "Student with ID: {} name update is successful".format(id),
#                 "Student name updated successfully",
#             )
#         return ErrorResponseModel(
#             "An error occurred",
#             404,
#             "There was an error updating the student data.",
#         )

# @router.delete("/{id}", response_description="Student data deleted from the database")
# async def delete_student_data(id: str):
#     if len(id) != 24:
#         return ErrorResponseModel("An error occurred", 404, "id length must be a 24-character hex string"        )
#     else:
#         deleted_student = await delete_student(id)
#         if deleted_student:
#             return ResponseModel(
#                 "Student with ID: {} removed".format(id), "Student deleted successfully"
#             )
#         return ErrorResponseModel(
#             "An error occurred", 404, "Student with id {0} doesn't exist".format(id)
#         )