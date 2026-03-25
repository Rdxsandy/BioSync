from pydantic import BaseModel, EmailStr
from typing import Optional

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str
    age: Optional[int]
    gender: Optional[str]
    height: Optional[float]
    weight: Optional[float]

class UserLogin(BaseModel):
    email: EmailStr
    password: str