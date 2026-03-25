from auth.service import register_user, login_user
from schema.user_schema import UserCreate

user = UserCreate(
    name="Test User",
    email="testuser@gmail.com",
    password="123456",
    age=22,
    gender="male",
    height=175,
    weight=70
)

print(register_user(user))

print(login_user("testuser@gmail.com", "123456"))