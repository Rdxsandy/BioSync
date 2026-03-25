from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional
#  user model 
class User(BaseModel):
    name: str
    email: EmailStr
    password: str
    age: Optional[int]
    gender: Optional[str]
    height: Optional[float]
    weight: Optional[float]
    created_at: datetime = datetime.utcnow()