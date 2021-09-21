from typing import Optional
from pydantic import BaseModel, Field


class BookSchema(BaseModel):
    title: str = Field(...)
    author: str = Field(...)
    genre: str = Field(...)
    description: str = Field(...)
    image_link: str = Field(...)
    favorite: Optional[bool] = None

    class Config:
        schema_extra = {
            "example": {
                "title": "The Great Gatsby",
                "author": "F. Scott Fitzgerald",
                "genre": "Fiction",
                "description": "A masterpiece of 20th century literature from F. Scott Fitzgerald, the preeminent chronicler of the Jazz Age--a term he coined. This classic work encapsulating the decadence and excess of the 1920s \"Jazz Age\" follows the unassuming Nick Carraway on his search for the American Dream, which leads him to the doorstep of Jay Gatsby, an enigmatic millionaire known for both his lavish parties and his undying love for Nick's cousin, the married Daisy Buchanan. With a mixture of envy and dismay, Nick observes Gatsby and his flamboyant life in the Long Island town of West Egg, while Gatsby yearns for Daisy and all that shimmers across the Sound in East Egg. The result is a chronicle of the drama and deceit that swirl around the lives of the wealthy, which cemented Fitzgeralds's reputation as the voice of his generation.",
                "image_link": "http://books.google.com/books/content?id=DF4NEAAAQBAJ&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api",
                "favorite": True
            }
        }

class UpdateBookModel(BaseModel):
    title: Optional[str]
    author: Optional[str]
    genre: Optional[str]
    description: Optional[str]
    image_link: Optional[str]
    favorite: Optional[bool]

    class Config:
        schema_extra = {
            "example": {
                "title": "The Great Gatsby",
                "author": "F. Scott Fitzgerald",
                "genre": "Fiction",
                "description": "A masterpiece of 20th century literature from F. Scott Fitzgerald, the preeminent chronicler of the Jazz Age--a term he coined. This classic work encapsulating the decadence and excess of the 1920s \"Jazz Age\" follows the unassuming Nick Carraway on his search for the American Dream, which leads him to the doorstep of Jay Gatsby, an enigmatic millionaire known for both his lavish parties and his undying love for Nick's cousin, the married Daisy Buchanan. With a mixture of envy and dismay, Nick observes Gatsby and his flamboyant life in the Long Island town of West Egg, while Gatsby yearns for Daisy and all that shimmers across the Sound in East Egg. The result is a chronicle of the drama and deceit that swirl around the lives of the wealthy, which cemented Fitzgeralds's reputation as the voice of his generation.",
                "image_link": "http://books.google.com/books/content?id=DF4NEAAAQBAJ&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api",
                "favorite": True
            }
        }
