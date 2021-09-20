from bson.objectid import ObjectId
import motor.motor_asyncio
from decouple import config

MONGO_DETAILS = config('MONGO_DETAILS')
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)
database = client.bookshelf

# DB Collections
user_collection = database.get_collection("user_collection")

# Helper functions to set up db data
def user_helper(user) -> dict:
    return {
        "first_name": user["first_name"],
        "last_name": user["last_name"],
        "username": user["username"],
        "password": user["password"],
        "is_active": user["is_active"],
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
# # Retrieve all users present in the database
# async def retrieve_users():
#     users = []
#     async for user in user_collection.find():
#         users.append(user_helper(user))
#     return users

# # Add a new user into to the database
# async def add_user(user_data: dict) -> dict:
#     user = await user_collection.insert_one(user_data)
#     new_user = await user_collection.find_one({"_id": user.inserted_id})
#     return user_helper(new_user)

# # Retrieve a user with a matching ID
# async def retrieve_user(id: str) -> dict:
#     user = await user_collection.find_one({"_id": ObjectId(id)})
#     if user:
#         return user_helper(user)

# # Update a user with a matching ID
# async def update_user(id: str, data: dict):
#     # Return false if an empty request body is sent.
#     if len(data) < 1:
#         return False
#     user = await user_collection.find_one({"_id": ObjectId(id)})
#     if user:
#         updated_user = await user_collection.update_one(
#             {"_id": ObjectId(id)}, {"$set": data}
#         )
#         if updated_user:
#             return True
#         return False

# # Delete a user from the database
# async def delete_user(id: str):
#     user = await user_collection.find_one({"_id": ObjectId(id)})
#     if user:
#         await user_collection.delete_one({"_id": ObjectId(id)})
#         return True