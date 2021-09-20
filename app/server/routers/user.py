from fastapi import APIRouter, Body, Response
from fastapi.encoders import jsonable_encoder
from ..models.user import UserSchema, UpdateUserModel, UserLoginSchema
from ..auth.auth_handler import signJWT

from ..database import (
    add_user,
    delete_user,
    retrieve_user,
    retrieve_users,
    update_user,
)
from ..models.user import (
    ErrorResponseModel,
    ResponseModel,
    UserSchema,
    UpdateUserModel,
)

router = APIRouter()

# users = []

# helper function to check to see if user exists
async def check_user(data: UserLoginSchema):
    users = await retrieve_users()
    for user in users:
        if user['username'] == data['username'] and user['password'] == data['password']:
            return True
    return False

# new user sign-up 
@router.post("/signup")
async def create_user(user: UserSchema = Body(...)):
    user = jsonable_encoder(user)
    new_user = await add_user(user)
    return signJWT(new_user)

# user login
@router.post("/login")
async def user_login(response: Response, user: UserLoginSchema = Body(...)):
    user = jsonable_encoder(user)
    if await check_user(user):
        token = signJWT(user)
        response.headers["Set-Cookie"]=f"token={token['access_token']}; Path=/; HttpOnly"
        return {"response": "user logged in"}
    return {
        "error": "Wrong login details!"
    }
