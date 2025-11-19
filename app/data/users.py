import pandas as pd
import sqlite3
def insert_data(conn, username, hashed_password):
    curr = conn.cursor()
    sql = ("""INSERT INTO users (username, password) VALUES (?,?)""")
    param = (username, hashed_password)
    curr.execute(sql, param)
    conn.commit()

def fetch_all_user(conn):
    curr = conn.cursor()
    sql = """ SELECT * FROM users """
    curr.execute(sql)
    rows = curr.fetchall()
    conn.close()
    return rows

def update_users(conn):
    curr = conn.cursor()
    curr.execute("""UPDATE users SET username = ? WHERE username is = ? """,('Polly_23','Barry'))
    conn.commit()
    curr.execute(""" SELECT username FROM users WHERE username = ?""",('Barry',))
    result = curr.fetchone()
    return f'Updated Result {result}'

def delete_users(conn):
    curr = conn.cursor
    curr.execute("""DELETE FROM users WHERE username = ?""",('Barry',))
    conn.commit()
    return f"Deleted User {curr.rowcount()}"

def get_all_users_pandas(conn):
    query = "SELECT * FROM users"
    df = pd.read_sql(query, conn)
    return df
