from database.db import users_collection
from schema.user_schema import UserCreate
from auth.utils import hash_password, verify_password, create_access_token


def register_user(user: UserCreate):
    existing_user = users_collection.find_one({"email": user.email})
    
    if existing_user:
        return {"error": "User already exists"}

    user_dict = user.model_dump()
    user_dict["password"] = hash_password(user.password)

    users_collection.insert_one(user_dict)

    return {"message": "User registered successfully"}


def login_user(email: str, password: str):
    user = users_collection.find_one({"email": email})

    if not user:
        return {"error": "Invalid email"}

    if not verify_password(password, user["password"]):
        return {"error": "Invalid password"}

    token = create_access_token({"user_id": str(user["_id"])})

    return {"access_token": token, "token_type": "bearer"}