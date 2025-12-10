import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from app.data.db import connect_database
import streamlit as st
from app.data.tickets import get_all_tickets_pandas, insert_data, update_tickets, delete_tickets
import pandas as pd

conn = connect_database()
st.title("IT Ticket Management")

# Protect Page
if "logged_in" not in st.session_state:
    st.error("You must log in first. Please go to the Login page from the sidebar.")
    st.stop()

query = get_all_tickets_pandas(conn)
df = pd.DataFrame(query)
st.subheader("All IT Support Tickets")
st.write(query)

with st.expander("Add New IT Ticket"):

    ticket_id = st.text_input("Ticket ID")
    priority = st.selectbox("Priority", ["Low", "Medium", "High", "Critical"])
    description = st.text_area("Description")
    status = st.selectbox("Status", ["Open", "In Progress", "Resolved"])
    assigned_to = st.text_input("Assigned To")
    created_at = st.text_input("Created At (YYYY-MM-DD HH:MM)")
    resolution_time_hours = st.number_input("Resolution Time (Hours)", min_value=0)

    if st.button("Add Ticket"):
        # Validate fields
        if not all([ticket_id, priority, description, status, assigned_to, created_at]):
            st.warning("All fields are required.")
        else:
            new_id = insert_data(
                ticket_id,
                priority,
                description,
                status,
                assigned_to,
                created_at,
                resolution_time_hours
            )
            st.success(f"Ticket successfully added! New ID: {new_id}")

with st.expander("Update Ticket"):
    available = df["ticket_id"].tolist()

    old_id = st.selectbox("Select ticket to update", available)
    new_id = st.text_input("New Ticket ID")

    if st.button("Update Ticket"):
        if not new_id:
            st.warning("Enter new ticket ID.")
        else:
            updated = update_tickets(old_id, new_id)
            if updated:
                st.success(f"Updated '{old_id}' → '{new_id}'")
            else:
                st.error("No ticket updated. Check ticket ID.")

with st.expander("Delete Ticket"):
    id_to_delete = st.selectbox("Select ticket", df["ticket_id"].tolist())

    if st.button("Delete Ticket"):
        deleted = delete_tickets(id_to_delete)

        if deleted:
            st.success(f"Deleted Ticket '{id_to_delete}'.")
        else:
            st.error("Ticket not found.")

st.header("📊 Ticket Analytics & Visual Insights")
if df.empty:
    st.info("No incident data available for analytics.")
else:
    st.subheader("Overview Metrics")

    col1, col2, col3 = st.columns(3)
    with col1:
        total_tickets = len(df)
        st.metric("Total Tickets", total_tickets)
    
    with col2:
        open_tickets = df[df["status"] == "Open"]
        st.metric("Open Tickets", len(open_tickets))
    
    with col3:
        avg_resolution = df["resolution_time_hours"].mean()
        st.metric("Avg. Resolution Time (Hours)", f"{avg_resolution:.2f}")
    
    st.subheader("Priority Distribution")
    priority_counts = df["priority"].value_counts()
    st.bar_chart(priority_counts)
    
    st.subheader("Status Distribution")
    status_counts = df["status"].value_counts()
    st.bar_chart(status_counts)

    st.subheader("Resolution Time Distribution")
    st.bar_chart(df["resolution_time_hours"])

