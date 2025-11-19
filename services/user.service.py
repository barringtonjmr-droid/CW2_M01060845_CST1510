import pandas as pd
import sqlite3
from app.users import insert_data
def migrate_info(conn):
    with open('DATA/users.txt', 'r') as f:
        users = f.readlines()
    for user in users:
        name, hash = (user.strip().split(',',1))
        insert_data(conn, name, hash)
    conn.close()

def migrate_cyber_incidents(conn):
    df = pd.read_csv('DATA/cyber_incidents.csv')
    df.to_sql('cyber_incidents', conn, if_exists='append', index=False)
    print('Data load')

def migrate_datasets_metadata(conn):
    df = pd.read_csv('DATA/datasets_metadata.csv')
    df.to_sql('datasets_metadata', conn, if_exists='append', index=False)
    print('Data load')
    
def migrate_it_tickets(conn):
    df = pd.read_csv('DATA/it_tickets.csv')
    df.to_sql('it_tickets', conn, if_exists='append', index=False)
    print('Data load')
