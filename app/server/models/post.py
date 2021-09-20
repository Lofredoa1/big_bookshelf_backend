from pydantic import BaseModel, Field


class PostSchema(BaseModel):
    id: int = Field(default=None)
    title: str = Field(...)
    content: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "title": "New Post",
                "content": "Post content"
            }
        }