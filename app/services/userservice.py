import bcrypt
import sqlite3
from pathlib import Path
from app.data.db import connect_database
from app.data.users import get_one_user, insert_data
import pandas as pd
DATA_DIR = Path('DATA')
path = DATA_DIR
def register_user(username, password):
    """Register new user with password hashing."""
    conn = connect_database()
    curr = conn.cursor()
    curr.execute("SELECT * FROM users WHERE username = ?", (username,))
    if curr.fetchone():
        conn.close()
        return False, f"Username '{username}' already exists."
    hashed_password = bcrypt.hashpw(password.encode('utf-8'),
                 bcrypt.gensalt()).decode('utf-8')
    insert_data(username, hashed_password)
    return True, f"User '{username} registered sucessfully."

def register_new_user(username, password, role='user'):
    """Register new user with password hashing."""
    conn = connect_database()
    curr = conn.cursor()
    curr.execute("SELECT * FROM users WHERE username = ?", (username,))
    if curr.fetchone():
        conn.close()
        return False, f"Username '{username}' already exists."
    hashed_password = bcrypt.hashpw(password.encode('utf-8'),
                 bcrypt.gensalt()).decode('utf-8')
    insert_data(username, hashed_password, role)
    return True, f"User '{username} registered sucessfully."

def login_user(username, password):
    """Authenticate user."""
    user = get_one_user(username)
    if not user:
        return False, "User not found"
    #Verify password
    stored_hash = user[2]
    if bcrypt.checkpw(password.encode('utf-8'), stored_hash.encode('utf-8')):
        return True, 'Login sucessfully'
    return False, "Incorrect password"  

def migrate_info(conn):
    with open('DATA/users.txt', 'r') as f:
        users = f.readlines()
    for user in users:
        name, hash = (user.strip().split(',',1))
        insert_data(conn, name, hash)
    conn.close()
def migrate_users_from_file(conn, filepath=path / "users.txt"):
    """Migrates users from users.txt to the database"""
    conn = connect_database("DATA/intelligence.db")
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