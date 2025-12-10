import sqlite3
import pandas as pd
from app.data.db import connect_database

def insert_data(incident_id, timestamp, severity, category, status, description):
    conn = connect_database()
    curr = conn.cursor()
    sql = ("""INSERT INTO cyber_incidents (incident_id, timestamp, severity, category, status, description ) VALUES (?,?,?,?,?,?)""")
    param = (incident_id, timestamp, severity, category, status, description)
    curr.execute(sql, param)
    conn.commit()
    incident_id = curr.lastrowid
    conn.close()
    return incident_id
def insert_incident(date, incident_type, severity, status, description, reported_by=None):
    conn = connect_database()
    curr = conn.cursor()
    sql = ("""INSERT INTO cyber_incident (date, incident_type, severity, status, description, reported_by) VALUES (?,?,?,?,?,?)""")
    param = (date, incident_type, severity, status, description, reported_by)
    curr.execute(sql, param)
    conn.commit()
    incident_id = curr.lastrowid
    conn.close()
    return incident_id


def fetch_all_user(conn):
    curr = conn.cursor()
    sql = """ SELECT * FROM cyber_incidents """
    curr.execute(sql)
    rows = curr.fetchall()
    conn.close()
    return rows

def update_users(conn):
    curr = conn.cursor()
    curr.execute("""UPDATE cyber_incidents SET incidents_id = ? WHERE incident_id is = ? """,(1001, 1010))
    conn.commit()
    curr.execute(""" SELECT incidents_id FROM cyber_incidents WHERE incident_id = ?""",(1010,))
    result = curr.fetchone()
    return f'Updated Result {result}'
def update_incidents(conn):
    conn = connect_database()
    curr = conn.cursor()
    curr.execute("""UPDATE cyber_incidents SET incident_id = ? WHERE incident_id = ?""",(1001, 1010))
    conn.commit()
    curr.execute("SELECT incident_id FROM cyber_incidents WHERE incident_id = ?",(1001,))
    result = curr.fetchone()
    return f"Updated Result: {result}"


def delete_users(conn):
    curr = conn.cursor
    curr.execute("""DELETE FROM cyber_incidents WHERE incident_id = ?""",('1010',))
    conn.commit()
    return f"Deleted User {curr.rowcount()}"
def delete_incidents(conn):
    curr = conn.cursor()
    curr.execute("DELETE FROM cyber_incidents WHERE incident_id = ?",(1010,))
    conn.commit()
    deleted = curr.rowcount
    return f"Deleted Rows: {deleted}"


def get_all_incidents_pandas(conn):
    query = "SELECT * FROM cyber_incidents"
    df = pd.read_sql(query, conn)
    conn.close()
    return df



