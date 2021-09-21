from typing import Optional
from fastapi import APIRouter, Body, Cookie
from fastapi.encoders import jsonable_encoder
from ..models.post import PostSchema, UpdatePostModel, CommentSchema
from ..auth.auth_handler import signJWT
from ..models.user import (
    ErrorResponseModel,
    ResponseModel,
)
from ..database import (
    retrieve_post,
    retrieve_posts,
    add_post,
    delete_post,
    update_post
)

router = APIRouter()

# Shows all posts
@router.get("/", response_description="All posts retrieved")
async def get_posts():
    posts = await retrieve_posts()
    if posts:
        return ResponseModel(posts, "All post data successfully retrieved")
    return ResponseModel(posts, "Empty list returned")

# Create a new post
@router.post("/", response_description="Post successfully created")
async def add_post_data(post: PostSchema = Body(...)):
    post = jsonable_encoder(post)
    new_post = await add_post(post)
    return ResponseModel(new_post, "Post successfully created")

# Get single post based on ID
@router.get("/{id}", response_description="Post data successfully retrieved")
async def get_single_post(id):
    if len(id) != 24:
        return ErrorResponseModel("An error occurred", 404, "id length must be a 24-character hex string")
    else:
        post = await retrieve_post(id)
        if post:
            return ResponseModel(post, "Post data retrieved successfully")
        return ErrorResponseModel("An error occurred.", 404, "Post doesn't exist.")

# Update a post based on ID
@router.put("/{id}")
async def update_post_data(id: str, req: UpdatePostModel = Body(...)):
    if len(id) != 24:
        return ErrorResponseModel("An error occurred", 404, "id length must be a 24-character hex string")
    else:
        req = {k: v for k, v in req.dict().items() if v is not None}
        updated_post = await update_post(id, req)
        if updated_post:
            return {"message": "Post with ID: {} has been updated successfully".format(id)}
        return ErrorResponseModel(
            "An error occurred",
            404,
            "There was an error updating the post data",
        )

# Destroy a post based on ID
@router.delete("/{id}", response_description="Post data deleted from the database")
async def delete_post_data(id: str):
    if len(id) != 24:
        return ErrorResponseModel("An error occurred", 404, "id length must be a 24-character hex string")
    else:
        deleted_post = await delete_post(id)
        if deleted_post:
            return {"message": "Post with ID: {} has been removed successfully".format(id)}
        return ErrorResponseModel(
            "An error occurred", 404, "Post with id {} doesn't exist".format(id)
        )

# Gets posts only from the local user
@router.get("/getuserposts")
async def get_users_post(token: Optional[str] = Cookie(None)) -> dict:
    print(token)
    return {
        "data": token
    }

# Gets posts only from the local user
@router.get("/getuserposts1")
async def get_users_post(token: Optional[str] = Cookie(None)) -> dict:
    print(token)
    return {
        "data": token
    }