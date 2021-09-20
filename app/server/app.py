from fastapi import FastAPI
from server.routers.post import router as PostRouter
from server.routers.user import router as UserRouter
from server.routers.book import router as BookRouter
from server.auth.auth_handler import signJWT

app = FastAPI()


app.include_router(PostRouter, tags=["Posts"], prefix="/posts")
app.include_router(UserRouter, tags=["User"], prefix="/user")
app.include_router(BookRouter, tags=["Book"], prefix="")

@app.get("/", tags=["root"])
async def read_root() -> dict:
    return {"message": "My first message"}