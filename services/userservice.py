import bcrypt
import sqlite3
from pathlib import Path
from database.db import connect_database
from app.data.users import insert_data
import pandas as pd
from services.database_manager import DatabaseManager
from models.user import User

#Object Oriented User Service
class UserService:
    def __init__(self, db_path: Path = Path("database") / "intelligence.db"):
        self.__db = DatabaseManager(db_path)
    
    def register_user(self, username: str, password: str):
        """Register new user with password hashing."""
        exists = self.__db.fetch_one(
            "SELECT 1 FROM users WHERE username = ?",
            (username,)
        )
        if exists:
            return False, f"Username '{username}' already exists."
        hashed_password = bcrypt.hashpw(
            password.encode("utf-8"),
            bcrypt.gensalt()
        ).decode("utf-8")
        created = self.__db.execute(
            "INSERT INTO users (username, password) VALUES (?, ?)",
            (username, hashed_password)
        )
        if created:
            return True, f"User '{username}' registered successfully."
        return False, "Registration failed due to a database error."
    
    def login_user(self, username: str, password: str):
        user_record = self.__db.fetch_one(
            "SELECT username, password FROM users WHERE username = ?",
            (username,)
        )
        if not user_record:
            return False, "User not found"
        username_db, stored_hash = user_record
        user = User(username_db, stored_hash)
        if user.validate_password(password):
            return True, user
        return False, "Incorrect password"


# Data Migration Functions
path1 = Path('DATA') / 'users.txt'
def migrate_info(conn):
    with open('DATA/users.txt', 'r') as f:
        users = f.readlines()
    for user in users:
        name, hash = (user.strip().split(',',1))
        insert_data(conn, name, hash)
    conn.close()

def migrate_users_from_file(conn, filepath=path1):
    """Migrates users from users.txt to the database"""
    conn = connect_database()
    if not filepath.exists():
        print(f':warning: File not found: {filepath}')
        print("No users to migrate.")
        return
    curr = conn.cursor()
    migrated_count = 0
    with open(filepath, 'r')as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            parts = line.split(',')
            if len(parts) >= 2:
                username = parts[0]
                password = parts[1]


                try:
                    curr.execute("INSERT OR IGNORE INTO users (username, password) VALUES (?,?)",
                                 (username, password))
                    if curr.rowcount > 0:
                        migrated_count += 1
                except sqlite3.Error as e:
                    print(f"Error migrating user {username}: {e}")
    
    conn.commit()
    print(f":white_check_mark: Migrated {migrated_count} users from {filepath.name}")

def migrate_cyber_incidents(conn):
    conn = connect_database()
    df = pd.read_csv('DATA/cyber_incidents.csv')
    df.to_sql('cyber_incidents', conn, if_exists='append', index=False)
    print('Data load')

def migrate_datasets_metadata(conn):
    conn = connect_database()
    df = pd.read_csv('DATA/datasets_metadata.csv')
    df.to_sql('datasets_metadata', conn, if_exists='append', index=False)
    print('Data load')
    
def migrate_it_tickets(conn):
    conn = connect_database()
    df = pd.read_csv('DATA/it_tickets.csv')
    df.to_sql('it_tickets', conn, if_exists='append', index=False)
    print('Data load')