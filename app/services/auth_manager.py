from app.services.database_manager import DatabaseManager
from pathlib import Path
import bcrypt
from models.user import User


DATA_DIR = Path("DATA")
DB_PATH = DATA_DIR / "intelligence.db"

class AuthManager:
    """Handles user registration and login"""

    def __init__(self, db_path: Path = DB_PATH):
        self.__db = DatabaseManager(db_path)

    def registers_user(self, username: str, password: str):
        """Register a new user."""
        exists = self.__db.fetch_one(
            "SELECT 1 FROM users WHERE username = ?",
            (username,)
        )
        if exists:
            return False, f"Username '{username}' already exists."

        hashed_password = bcrypt.hashpw(
            password.encode('utf-8'),
            bcrypt.gensalt()
        ).decode('utf-8')

        created = self.__db.execute(
            "INSERT INTO users (username, password) VALUES (?, ?)",
            (username, hashed_password)
        )

        if created:
            return True, f"User '{username}' registered successfully."
        else:
            return False, "Registration failed due to a database error."

    def login_user(self, username: str, password: str):
        """Authenticate user using User class."""
        user_record = self.__db.fetch_one(
            "SELECT username, password FROM users WHERE username = ?",
            (username,)
        )

        if not user_record:
            return False, "User not found."

        username_db, password_hash_db = user_record

        # Instantiate User object using stored hash
        user_obj = User(username_db, password_hash_db)

        # Validate password using User.validate_password()
        if user_obj.validate_password(password):
            return True, user_obj  # return the full user object

        return False, "Incorrect password."
