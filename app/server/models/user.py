from pydantic import BaseModel, Field
from typing import Optional

class UserSchema(BaseModel):
    first_name: str = Field(...)
    last_name: str = Field(...)
    username: str = Field(...)
    password: str = Field(...)
    is_active: Optional[bool] = None
    posts: list 

    class Config:
        schema_extra = {
            "example": {
                "first_name": "Babe",
                "last_name": "Ruth",
                "username": "TheGreatBambino",
                "password": "weakpassword",
                "is_active": True
            }
        }

class UpdateUserModel(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    username: Optional[str]
    password: Optional[int]
    is_active: Optional[bool]

    class Config:
        schema_extra = {
            "example": {
                "first_name": "Babe",
                "last_name": "Ruth",
                "username": "TheGreatBambino",
                "password": "weakpassword",
                "is_active": True
            }
        }

class UserLoginSchema(BaseModel):
    username: str = Field(...)
    password: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "username": "TheGreatBambino",
                "password": "weakpassword"
            }
        }

class UserInDB(UserSchema):
    hashed_password: str

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None


def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}