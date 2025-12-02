import sqlite3
from pathlib import Path

DATA_DIR = Path('DATA')
path = DATA_DIR / "intelligence.db"
def connect_database(db_path=path):
    """Connect to SQLite database."""
    return sqlite3.connect(str(db_path))
