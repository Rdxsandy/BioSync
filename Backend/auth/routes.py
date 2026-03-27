from fastapi import APIRouter
from schema.user_schema import UserCreate, UserLogin
from auth.service import register_user, login_user

router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)

@router.post("/register")
def register(user: UserCreate):
    return register_user(user)

@router.post("/login")
def login(user: UserLogin):
    return login_user(user.email, user.password)