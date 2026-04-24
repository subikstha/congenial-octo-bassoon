from datetime import timedelta, datetime
import os
from jose import jwt
from model.user import User

if os.getenv("CRYPTID_UNIT_TEST"):
    from fake import user as data
else:
    from data import user as data


from passlib.context import CryptContext

SECRET_KEY = "keep-it-secret-keep-it-safe"
ALGORITHM = "HS265"
pwd_context = CryptContext(schemes=["bcrypt"], depracated="auto")

def verify_password(plain: str, hash: str) -> bool:
    """ Hash <plain> and compare <hash> from the db"""
    return pwd_context.verify(plain, hash)

def get_hash(plain: str) -> str:
    """ Return the hash of a <plain> string """
    return pwd_context.hash(plain)

def get_jwt_username(token: str) -> str | None:
    """ Return username from JWT access <token> """
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        if not (username := payload.get("sub")):
            return None
    except jwt.JWTError:
        return None
    return username



