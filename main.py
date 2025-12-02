from app.data.db import connect_database
from app.data.schema import create_all_tables
from app.services.userservice import register_user, login_user, migrate_users_from_file
from app.data.incidents import insert_incident, get_all_incidents_pandas

def main():
    print("=" * 60)
    print("Week 8: Database Demo")
    print("=" * 60)

conn = connect_database('DATA/intelligence.db')
create_all_tables(conn)
conn.close()

migrate_users_from_file(conn)

success, msg = register_user("alice", "SecurePass123!")
print(msg)
sucess, msg = login_user("alice", "SecurePass123!")
print(msg)

incident_id = insert_incident(
    "2024-11-05",
    "Phishing",
    "High",
    "Open",
    "Suspicious email detected",
    "alice"
)
print(f"Created incident #{incident_id}")

df = get_all_incidents_pandas(conn)
print(f"Total incidents: {len(df)}")

if __name__ == "__main__":
    main() 
