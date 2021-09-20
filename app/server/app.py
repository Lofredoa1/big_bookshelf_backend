from datetime import datetime, timedelta
from fastapi import FastAPI, Depends, HTTPException, status
from .routers.post import router as PostRouter
from .routers.user import router as UserRouter
from .routers.book import router as BookRouter
from .auth.auth_handler import signJWT
from .models.user import Token
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm


app = FastAPI()


app.include_router(PostRouter, tags=["Posts"], prefix="/posts")
app.include_router(UserRouter, tags=["User"], prefix="/user")
app.include_router(BookRouter, tags=["Book"], prefix="")

@app.get("/", tags=["root"])
async def read_root() -> dict:
    return {"message": "My first message"}


# @app.post("/token", response_model=Token)
# async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
#     user = await authenticate_user(form_data.username, form_data.password)
#     print("HERE", user)
#     if not user:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Incorrect username or password",
#             headers={"WWW-Authenticate": "Bearer"},
#         )
#     access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
#     access_token = create_access_token(
#         data={"sub": user['username']}, expires_delta=access_token_expires
#     )
#     return {"access_token": access_token, "token_type": "bearer"}
