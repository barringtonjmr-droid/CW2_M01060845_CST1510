
from services.database_manager import DatabaseManager, DB_PATH
from services.userservice import UserService
from pathlib import Path

class AuthManager:
    """Handles user registration and login"""

    def __init__(self, db_path: Path = DB_PATH):
        self.__db = DatabaseManager(db_path)
        self.__user_service = UserService(db_path)

    def registers_user(self, username: str, password: str):
        """Register a new user."""
        return self.__user_service.register_user(username, password)

    def login_user(self, username: str, password: str):
        """Authenticate user."""
        return self.__user_service.login_user(username, password)