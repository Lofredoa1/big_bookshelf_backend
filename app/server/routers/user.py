from fastapi import APIRouter, Body, Response, HTTPException
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

# helper function to prevent duplicate usernames
async def check_username(data: UserSchema):
    users = await retrieve_users()
    if (len(users) < 1):
        return True
    else:
        print("Step 2", users)
        for user in users:
            if data['username'] == user['username']:
                return False
            # else:
            #     print("??????")
            #     return False
        
# new user sign-up 
@router.post("/signup", response_description="User successfully created.")
async def create_user(user: UserSchema = Body(...)):
    user = jsonable_encoder(user)
    print("step 1", user)
    if await check_username(user):
        new_user = await add_user(user)
        return signJWT(new_user)
    # return {
    #     "error": "Username already exists."
    # }
    raise HTTPException(status_code = 406, detail="Username already exists")

# user login
@router.post("/login", response_description="User successfully logged in.")
async def user_login(response: Response, user: UserLoginSchema = Body(...)):
    user = jsonable_encoder(user)
    if await check_user(user):
        token = signJWT(user)
        response.set_cookie(key="token", value=f"token={token}; Path=/; HttpOnly; Domain=app.localhost")
        # response.headers["Set-Cookie"]=f"token={token}; Path=/; HttpOnly"
        return {"response": "user logged in"}
    return {
        "error": "Wrong login details!"
    }
