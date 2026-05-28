from fastapi import HTTPException, status
from database.db import users_collection
from schema.user_schema import UserCreate
from auth.utils import hash_password, verify_password, create_access_token


def register_user(user: UserCreate):
    existing_user = users_collection.find_one({"email": user.email})
    
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User already exists"
        )

    user_dict = user.model_dump()
    user_dict["password"] = hash_password(user.password)

    users_collection.insert_one(user_dict)

    return {"message": "User registered successfully"}


def login_user(email: str, password: str):
    user = users_collection.find_one({"email": email})

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password"
        )

    if not verify_password(password, user["password"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password"
        )

    token = create_access_token({"user_id": str(user["_id"])})

    return {"access_token": token, "token_type": "bearer"}