
def create_db(conn):
    curr = conn.cursor()
    sql = (""" CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL) """)

    curr.execute(sql)
    conn.commit()