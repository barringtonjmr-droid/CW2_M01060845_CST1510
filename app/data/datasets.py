import pandas as pd
import sqlite3
def insert_data(conn, dataset_id, name, rows, columns, uploaded_by, upload_date):
    curr = conn.cursor()
    sql = ("""INSERT INTO datasets_metadata (dataset_id, name, rows, columns, uploaded_by, upload_date) VALUES (?,?,?,?,?,?)""")
    param = (dataset_id, name, rows, columns, uploaded_by, upload_date)
    curr.execute(sql, param)
    conn.commit()

def fetch_all_user(conn):
    curr = conn.cursor()
    sql = """ SELECT * FROM datasets_metadata """
    curr.execute(sql)
    rows = curr.fetchall()
    conn.close()
    return rows

def update_users(conn):
    curr = conn.cursor()
    curr.execute("""UPDATE datasets_metadata SET name = ? WHERE dataset_id is = ? """,('Monetary_Development', 2))
    conn.commit()
    curr.execute(""" SELECT name FROM datasets_metadata WHERE dataset_id = ?""",(2,))
    result = curr.fetchone()
    return f'Updated Result {result}'

def delete_users(conn):
    curr = conn.cursor
    curr.execute("""DELETE FROM datasets_metadata WHERE dataset_id = ?""",(2,))
    conn.commit()
    return f"Deleted User {curr.rowcount()}"

def get_all_users_pandas(conn):
    query = "SELECT * FROM datasets_metadata"
    df = pd.read_sql(query, conn)
    return df
