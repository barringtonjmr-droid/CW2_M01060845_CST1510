import sqlite3
from pathlib import Path
import os

# Default database path (relative to project root)
DEFAULT_DB_DIR = Path('database')
DB_PATH = DEFAULT_DB_DIR / "intelligence.db"


class DatabaseManager:
    def __init__(self, db_path: Path = None):
        # Resolve a sensible absolute path: if a relative path is passed,
        # interpret it relative to the project root (one level above this file).
        if db_path is None:
            project_root = Path(__file__).resolve().parents[1]
            db_path = project_root / DB_PATH

        self.__db_path = Path(db_path)

        # Ensure the database directory exists
        try:
            db_parent = self.__db_path.parent
            if not db_parent.exists():
                db_parent.mkdir(parents=True, exist_ok=True)
        except Exception as e:
            print(f"[DatabaseManager] Could not create DB directory {self.__db_path.parent}: {e}")

        self.__connection = None
        # Try to connect immediately and log the resolved path for diagnostics 
        self.connect()

    def connect(self):
        """Create a database connection."""
        try:
            # Open connection (create file if it does not exist)
            self.__connection = sqlite3.connect(str(self.__db_path))
            return self.__connection
        except sqlite3.Error as e:
            # Print helpful diagnostics
            try:
                exists = self.__db_path.exists()
                mode = oct(os.stat(self.__db_path).st_mode) if exists else 'n/a'
            except Exception:
                exists = False
                mode = 'n/a'
            print(f"SQLite Error: {e} -- path={self.__db_path} exists={exists} mode={mode}")
            return None

    def execute(self, sql: str, params: tuple = ()):
        """Execute a write query (INSERT, UPDATE, DELETE)."""
        if not self.__connection:
            self.connect()
        cur = self.__connection.cursor()
        cur.execute(sql, params)
        self.__connection.commit()
        return cur
    
    def fetch_one(self, sql: str, params: tuple = ()):
        """Fetch a single user"""
        if not self.__connection:
            self.connect()
        cur = self.__connection.cursor()
        cur.execute(sql, params)
        return cur.fetchone()
    
    def fetch_all(self, sql:str, params: tuple = ()):
        """Fetch all users"""
        if not self.__connection:
            self.connect()
        cur = self.__connection.cursor()
        cur.execute(sql, params)
        return cur.fetchall()
    
    def close(self):
        """Closes the database connection"""
        if self.__connection:
            self.__connection.close()
            self.__connection = None
    