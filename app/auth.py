
from fastapi import Request, HTTPException
from starlette.middleware.sessions import SessionMiddleware
from fastapi.responses import RedirectResponse
from fastapi.security import OAuth2PasswordRequestForm
from passlib.context import CryptContext

# Simple password hasher
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# In-memory user for demo
USERS = {
    "admin": pwd_context.hash("admin123")
}

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_current_user(request: Request):
    user = request.session.get("user")
    if not user:
        raise HTTPException(status_code=403, detail="Not authenticated")
    return user

def authenticate_user(username: str, password: str):
    if username in USERS and verify_password(password, USERS[username]):
        return username
    return None
