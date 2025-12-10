import sqlite3
import pathlib as Path

class DatabaseManager:
    def __init__(self, db_path: Path):
        self.__db_path = db_path
        self.__connection = None
        self.connect()


    def connect(self):
        """Create a Database connection"""
        try:
            self.__connection = sqlite3.connect(str(self.__db_path))
            return self.__connection
        
        except sqlite3.Error as e:
            print(f"Sqlite Error: {e}")
    
    def execute(self, sql: str, params: tuple = ()):
        """Execute a write query (INSERT, UPDATE, DELETE)."""
        cur = self.__connection.cursor()
        cur.execute(sql, params)
        self.__connection.commit()
        return cur
    
    def fetch_one(self, sql: str, params: tuple = ()):
        """Fetch one user"""
        cur = self.__connection.cursor()
        cur.execute(sql, params)
        return cur.fetchone()
    
    def fetch_all(self, sql:str, params: tuple = ()):
        """Fetch all users"""
        cur = self.__connection.cursor()
        cur.execute(sql, params)
        return cur.fetchall()
    
    def close(self):
        """Closes the database connection"""
        if self.__connection:
            self.__connection.close()
            self.__connection = None
    def get_connection(self):
        """Return the current database connection"""
        return self.__connection
    def __del__(self):
        self.close()
