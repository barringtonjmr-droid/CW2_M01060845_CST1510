import pandas as pd
import sqlite3
def insert_data(conn, ticket_id, priority, description, status, assigned_to, created_at, resolution_time_hours):
    curr = conn.cursor()
    sql = ("""INSERT INTO datasets_metadata (ticket_id, priority, description, status, assigned_to, created_at, resolution_time_hours) VALUES (?,?,?,?,?,?,?)""")
    param = (ticket_id, priority, description, status, assigned_to, created_at, resolution_time_hours)
    curr.execute(sql, param)
    conn.commit()

def fetch_all_user(conn):
    curr = conn.cursor()
    sql = """ SELECT * FROM it_tickets """
    curr.execute(sql)
    rows = curr.fetchall()
    conn.close()
    return rows

def update_users(conn):
    curr = conn.cursor()
    curr.execute("""UPDATE it_tickets SET priority = ? WHERE ticket_id is = ? """,('Critical', 2005))
    conn.commit()
    curr.execute(""" SELECT priority FROM it_tickets WHERE ticket_id = ?""",(2005,))
    result = curr.fetchone()
    return f'Updated Result {result}'

def delete_users(conn):
    curr = conn.cursor
    curr.execute("""DELETE FROM it_tickets WHERE ticket_id = ?""",(2005,))
    conn.commit()
    return f"Deleted User {curr.rowcount()}"

def get_all_users_pandas(conn):
    query = "SELECT * FROM it_tickets"
    df = pd.read_sql(query, conn)
    return df
