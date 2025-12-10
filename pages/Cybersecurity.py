import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from app.data.db import connect_database
import streamlit as st
from app.data.incidents import get_all_incidents_pandas, insert_data, update_incidents, delete_incidents
import pandas as pd



conn = connect_database()
st.title(" Cybersecurity Management")

# Protect Page
if "logged_in" not in st.session_state:
    st.error("You must log in first. Please go to the Login page from the sidebar.")
    st.stop()

query = get_all_incidents_pandas(conn)
df = pd.DataFrame(query)

st.subheader("All Cybersecurity Incidents")
st.write(query)
with st.expander("Add New Cyber Incident"):

    incident_id = st.text_input("Incident ID")
    timestamp = st.text_input("Timestamp (YYYY-MM-DD HH:MM)")
    severity = st.selectbox("Severity", ["Low", "Medium", "High", "Critical"])
    category = st.text_input("Category (e.g., Malware, Phishing, DDoS)")
    status = st.selectbox("Status", ["Open", "Investigating", "Resolved"])
    description = st.text_area("Description")

    if st.button("Add Incident"):
        # Validate fields
        if not all([incident_id, timestamp, severity, category, status, description]):
            st.warning("All fields are required.")
        else:
            new_id = insert_data(
                incident_id,
                timestamp,
                severity,
                category,
                status,
                description
            )
            st.success(f"Incident successfully added! New ID: {new_id}")

with st.expander("Update Incident"):
    available = df["incident_id"].tolist()

    old_id = st.selectbox("Select user to update", available)
    new_id = st.text_input("New Incident ID")

    if st.button("Update Incident"):
        if not new_id:
            st.warning("Enter new incident.")
        else:
            updated = update_incidents(old_id, new_id)
            if updated:
                st.success(f"Updated '{old_id}' → '{new_id}'")
            else:
                st.error("No user updated. Check incidents.")

with st.expander("Delete Incident"):
    id_to_delete = st.selectbox("Select incident", df["incident_id"].tolist())

    if st.button("Delete Incident"):
        deleted = delete_incidents(id_to_delete)

        if deleted:
            st.success(f"Deleted Incident '{id_to_delete}'.")
        else:
            st.error("Incident not found.")

st.header("📊 Incident Analytics & Visual Insights")

if df.empty:
    st.info("No incident data available for analytics.")
else:
    st.subheader("Overview Metrics")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Total Incidents", len(df))

    with col2:
        high_severity = df[df["severity"] == "High"]
        st.metric("High Severity Incidents", len(high_severity))

    with col3:
        open_incidents = df[df["status"].str.lower() == "open"]
        st.metric("Open Incidents", len(open_incidents))

 
    st.subheader("🔥 Incident Severity Distribution")
    severity_counts = df["severity"].value_counts()
    st.bar_chart(severity_counts)

    st.subheader("📂 Incident Category Breakdown")
    category_counts = df["category"].value_counts()
    st.bar_chart(category_counts)

    st.subheader("📌 Incident Status Overview")
    status_counts = df["status"].value_counts()
    st.bar_chart(status_counts)

    if "timestamp" in df.columns:
        st.subheader("⏱ Incident Timeline (by Date)")
        
        df["date"] = pd.to_datetime(df["timestamp"]).dt.date
        timeline_counts = df["date"].value_counts().sort_index()
        st.line_chart(timeline_counts)