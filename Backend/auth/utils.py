import os
import bcrypt as _bcrypt
from dotenv import load_dotenv
from jose import jwt
from datetime import datetime, timedelta, timezone

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"

# token valid for 7 days
ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7


def _truncate_password(password: str) -> bytes:
    """Encode password to UTF-8 and truncate to 72 bytes (bcrypt hard limit)."""
    encoded = password.encode("utf-8")
    return encoded[:72]


def hash_password(password: str) -> str:
    """Hash a password using bcrypt directly (avoids passlib's 72-byte check)."""
    pw_bytes = _truncate_password(password)
    hashed = _bcrypt.hashpw(pw_bytes, _bcrypt.gensalt())
    return hashed.decode("utf-8")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verify a password against its bcrypt hash."""
    pw_bytes = _truncate_password(plain_password)
    try:
        return _bcrypt.checkpw(pw_bytes, hashed_password.encode("utf-8"))
    except Exception:
        return False


def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )
    to_encode.update({"exp": expire})
    token = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return token