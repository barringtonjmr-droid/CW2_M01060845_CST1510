
def create_table(conn):
    curr = conn.cursor()
    sql = (""" CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL,
    role TEXT DEFAULT 'user') """)
    curr.execute(sql)
    conn.commit()
    print(":white_check_mark: Users table created successfully")
def create_cyber_incidents_table(conn):
    """Create cyber incidents table"""
    curr = conn.cursor()
    sql = ("""CREATE TABLE IF NOT EXISTS cyber_incident (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT, 
    incident_type TEXT,
    severity TEXT,
    status TEXT,
    description TEXT,
    reported_by TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)""")
    curr.execute(sql)
    conn.commit()
    print(":white_check_mark: Cyber incidents table created successfully")

def create_datasets_metadata_table(conn):
    """Create datasets table"""
    curr = conn.cursor()
    sql = ("""CREATE TABLE IF NOT EXISTS datasets_metadata (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    dataset_name TEXT, 
    category TEXT,
    source TEXT,
    last_updated TEXT,
    record_count TEXT,
    file_size_mb TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)""")
    curr.execute(sql)
    conn.commit()
    print(":white_check_mark: datasets table created successfully")
def create_it_tickets_table(conn):
    """Create tickets table"""
    curr = conn.cursor()
    sql = ("""CREATE TABLE IF NOT EXISTS cyber_incidents (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ticket_id TEXT UNIQUE NOT NULL, 
    priority TEXT,
    status TEXT,
    category TEXT,
    subject TEXT NOT NULL,
    description TEXT,
    created_date TEXT,
    resolved_date TEXT,
    assigned_to TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)""")
    curr.execute(sql)
    conn.commit()
    print(":white_check_mark: IT tickets table created successfully")
def create_all_tables(conn):
    """Create all tables"""
    create_table(conn)
    create_cyber_incidents_table(conn)
    create_datasets_metadata_table(conn)
    create_it_tickets_table(conn)