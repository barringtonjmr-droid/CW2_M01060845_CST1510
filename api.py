import bcrypt
from app.data.db import conn
from app.data.users import insert_data
from app.data.users import get_one_user

def hash_password(pwd):
    """Hash password"""
    password_bytes = pwd.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed_pwd = bcrypt.hashpw(password_bytes, salt)
    return hashed_pwd.decode('utf-8')  

def validate_password(pwd, hashed_pwd):
    password_bytes = pwd.encode('utf-8')
    hashed_pwd_bytes = hashed_pwd.encode('utf-8')
    return bcrypt.checkpw(password_bytes, hashed_pwd_bytes)


    

