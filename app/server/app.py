from datetime import datetime, timedelta
from fastapi import FastAPI, Depends, HTTPException, status
from .routers.post import router as PostRouter
from .routers.user import router as UserRouter
from .routers.book import router as BookRouter
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(PostRouter, tags=["Posts"], prefix="/post")
app.include_router(UserRouter, tags=["User"], prefix="/user")
app.include_router(BookRouter, tags=["Book"], prefix="/book")

@app.get("/", tags=["root"])
async def read_root() -> dict:
    return {"message": "My first message"}