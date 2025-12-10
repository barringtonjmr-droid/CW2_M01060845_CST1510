import sqlite3
import pathlib as Path

class DatabaseManager:
    def __init__(self, db_path: Path):
        self.db_path = db_path
        self.connection = None
        self.connect()


    def connect(self):
        """Create a Database connection"""
        try:
            self.connection = sqlite3.connect(str(self.db_path))
            return self.connection
        
        except sqlite3.Error as e:
            print(f"Sqlite Error: {e}")
    
    def execute(self, sql: str, params: tuple = ()):
        """Execute a write query (INSERT, UPDATE, DELETE)."""
        cur = self.connection.cursor()
        cur.execute(sql, params)
        self.connection.commit()
        return cur
    
    def fetch_one(self, sql: str, params: tuple = ()):
        """Fetch one user"""
        cur = self.connection.cursor()
        cur.execute(sql, params)
        return cur.fetchone()
    
    def fetch_all(self, sql:str, params: tuple = ()):
        """Fetch all users"""
        cur = self.connection.cursor()
        cur.execute(sql, params)
        return cur.fetchall()
    
    def close(self):
        """Closes the database connection"""
        if self.connection:
            self.connection.close()
            self.connection = None
