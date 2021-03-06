from bson.objectid import ObjectId
import motor.motor_asyncio
from decouple import config

MONGO_DETAILS = config('MONGO_DETAILS')
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)
database = client.bookshelf

# DB Collections
user_collection = database.get_collection("user_collection")
book_collection = database.get_collection("book_collection")
post_collection = database.get_collection("post_collection")
comment_collection = database.get_collection("comment_collection")

# Helper functions to set up db data models
def user_helper(user) -> dict:
    return {
        "id": str(user["_id"]),
        "first_name": user["first_name"],
        "last_name": user["last_name"],
        "username": user["username"],
        "password": user["password"],
        "is_active": user["is_active"],
    }

def book_helper(book) -> dict:
    return {
        "id": str(book["_id"]),
        "title": book["title"],
        "author": book["author"],
        "genre": book["genre"],
        "description": book["description"],
        "image_link": book["image_link"],
        "favorite": book["favorite"],
    }

def post_helper(post) -> dict:
    return {
        "id": str(post["_id"]),
        "title": post["title"],
        "content": post["title"],
        "likes": post["likes"],
        "comments": post["comments"],
    }

def comment_helper(comment) -> dict:
    return {
        "id": str(comment["_id"]),
        "username": comment["username"],
        "content": comment["content"],
        "likes": comment["likes"],
    }

############### User ###################
# Retrieve all users present in the database
async def retrieve_users():
    users = []
    async for user in user_collection.find():
        users.append(user_helper(user))
    return users

# Add a new user into to the database
async def add_user(user_data: dict) -> dict:
    user = await user_collection.insert_one(user_data)
    new_user = await user_collection.find_one({"_id": user.inserted_id})
    return user_helper(new_user)

# Retrieve a user with a matching ID
async def retrieve_user(id: str) -> dict:
    user = await user_collection.find_one({"_id": ObjectId(id)})
    if user:
        return user_helper(user)

# Update a user with a matching ID
async def update_user(id: str, data: dict):
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False
    user = await user_collection.find_one({"_id": ObjectId(id)})
    if user:
        updated_user = await user_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_user:
            return True
        return False

# Delete a user from the database
async def delete_user(id: str):
    user = await user_collection.find_one({"_id": ObjectId(id)})
    if user:
        await user_collection.delete_one({"_id": ObjectId(id)})
        return True

############### Book ###################
# Retrieve all books present in the database
async def retrieve_books():
    books = []
    async for book in book_collection.find():
        books.append(book_helper(book))
    return books

# Add a new book into to the database
async def add_book(book_data: dict) -> dict:
    book = await book_collection.insert_one(book_data)
    new_book = await book_collection.find_one({"_id": book.inserted_id})
    return book_helper(new_book)

# Retrieve a book with a matching ID
async def retrieve_book(id: str) -> dict:
    book = await book_collection.find_one({"_id": ObjectId(id)})
    if book:
        return book_helper(book)

# Update a book with a matching ID
async def update_book(id: str, data: dict):
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False
    book = await book_collection.find_one({"_id": ObjectId(id)})
    if book:
        updated_book = await book_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_book:
            return True
        return False

# Delete a book from the database
async def delete_book(id: str):
    book = await book_collection.find_one({"_id": ObjectId(id)})
    if book:
        await book_collection.delete_one({"_id": ObjectId(id)})
        return True

############### Post ###################
# Retrieve all posts present in the database
async def retrieve_posts():
    posts = []
    async for post in post_collection.find():
        posts.append(post_helper(post))
    return posts

# Add a new post into to the database
async def add_post(post_data: dict) -> dict:
    post = await post_collection.insert_one(post_data)
    new_post = await post_collection.find_one({"_id": post.inserted_id})
    return post_helper(new_post)

# Retrieve a post with a matching ID
async def retrieve_post(id: str) -> dict:
    post = await post_collection.find_one({"_id": ObjectId(id)})
    if post:
        return post_helper(post)

# Update a post with a matching ID
async def update_post(id: str, data: dict):
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False
    post = await post_collection.find_one({"_id": ObjectId(id)})
    if post:
        updated_post = await post_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_post:
            return True
        return False

# Delete a post from the database
async def delete_post(id: str):
    post = await post_collection.find_one({"_id": ObjectId(id)})
    if post:
        await post_collection.delete_one({"_id": ObjectId(id)})
        return True