import bcrypt

class User:
    def __init__(self, username:str, password:str):
        self.__username = username
        self.__password = password
    
    def get_username(self) -> str:
        return self.__username
    
    def get_password(self) -> str:
        return self.__password

    def validate_password(self, pwd: str) -> bool:
        password_bytes = pwd.encode('utf-8')
        hashed_bytes = self.__password.encode('utf-8')
        return bcrypt.checkpw(password_bytes, hashed_bytes)
    
    def __str__(self) -> str:
        return f"User ({self.__username})"