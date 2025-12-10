import pandas as pd
from app.data.db import connect_database
def insert_data(username, password):
    conn = connect_database()
    curr = conn.cursor()
    sql = ("""INSERT INTO users (username, password) VALUES (?,?)""")
    param = (username, password)
    curr.execute(sql, param)
    conn.commit()
    conn.close()

def insert_user_data(username, password, role='user'):
    conn = connect_database()
    curr = conn.cursor()
    sql = ("""INSERT INTO users (username, password, role) VALUES (?,?,?)""")
    param = (username, password, role)
    curr.execute(sql, param)
    conn.commit()
    conn.close()

def fetch_all_user(conn):
    conn = connect_database()
    curr = conn.cursor()
    sql = """ SELECT * FROM users """
    curr.execute(sql)
    rows = curr.fetchall()
    conn.close()
    return rows

def update_users(conn):
    conn = connect_database()
    curr = conn.cursor()
    curr.execute("""UPDATE users SET username = ? WHERE username is = ? """,('Polly_23','Barry'))
    conn.commit()
    curr.execute(""" SELECT username FROM users WHERE username = ?""",('Barry',))
    result = curr.fetchone()
    return f'Updated Result {result}'

def delete_users(conn):
    conn = connect_database()
    curr = conn.cursor()
    curr.execute("""DELETE FROM users WHERE username = ?""",('Barry',))
    conn.commit()
    return f"Deleted User {curr.rowcount()}"

def get_all_users_pandas(conn):
    query = "SELECT * FROM users"
    df = pd.read_sql(query, conn)
    conn.close()
    return df
def get_one_user(username):
    """Retrieve user by username"""
    conn = connect_database()
    curr = conn.cursor()
    curr.execute("SELECT * FROM users WHERE username = ?", (username,))
    user = curr.fetchone()
    conn.close()
    return user

def verify_user(conn):
    conn = connect_database
    curr = conn.execute()
    curr.execute("SELECT id, username, role FROM USERS")
    users = curr.fetchall()
    print("Users in database:")
    print(f"{'ID' :<5} {'Username':<15} {'Role':<10}")
    print("-" * 35)
    for user in users:
        print(f"{user[0]:<5} {user[1]:<15} {user[2]:<10}")
    print(f"\nTotal users: {len(users)}")
    conn.close()