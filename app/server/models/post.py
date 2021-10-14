from typing import Optional
from pydantic import BaseModel, Field

class CommentSchema(BaseModel):
    username: str = Field(...)
    content: str = Field(...)
    likes: int = Field(default=0)

    class Config:
        schema_extra = {
            "example": {
                "username": "TheGreatBambino",
                "content": "That would be me.",
                "likes": 100
            }
        }

class PostSchema(BaseModel):
    title: str = Field(...)
    content: str = Field(..., max_length=300)
    likes: int = Field(default=0)
    userId: str=Field(...)
    comments: set[CommentSchema] = None

    class Config:
        schema_extra = {
            "example": {
                "title": "Who is the Greatest Baseball Player?",
                "content": "Everyone comment below.",
                "likes": 0,
                "comments": None
            }
        }

class UpdatePostModel(BaseModel):
    title: Optional[str]
    content: Optional[str]
    likes: Optional[int]
    userId: Optional[str]
    comments: Optional[set]
    

    class Config:
        schema_extra = {
            "example": {
                "title": "Who is the Greatest Baseball Player?",
                "content": "Everyone comment below.",
                "likes": 0,
                "comments": None
            }
        }

