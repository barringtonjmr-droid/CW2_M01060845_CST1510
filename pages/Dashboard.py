import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

import streamlit as st
import pandas as pd
from app.data.db import connect_database
from app.data.users import (
    insert_data,
    update_users,
    delete_users,   
    get_all_users_pandas
)
conn = connect_database()
st.title("User Management Dashboard")

# Protect Page
if "logged_in" not in st.session_state:
    st.error("You must log in first. Please go to the Login page from the sidebar.")
    st.stop()


query = get_all_users_pandas(conn)
df = pd.DataFrame(query)
st.subheader("All Users")
st.write(query)


with st.expander("Add New User"):
    username = st.text_input("New Username", key="add_new_username")
    password = st.text_input("New Password", type="password")

    if st.button("Create User"):
        if not username or not password:
            st.warning("All fields required.")
        else:
            insert_data(username, password)
            st.success(f"User '{username}' added! Refresh page.")


with st.expander("Update User"):
    available = df["username"].tolist()

    old_name = st.selectbox("Select user to update", available)
    new_name = st.text_input("New Username")

    if st.button("Update User"):
        if not new_name:
            st.warning("Enter new username.")
        else:
            updated = update_users(old_name, new_name)
            if updated:
                st.success(f"Updated '{old_name}' → '{new_name}'")
            else:
                st.error("No user updated. Check username.")


with st.expander("Delete User"):
    user_to_delete = st.selectbox("Select user", df["username"].tolist())

    if st.button("Delete User"):
        deleted = delete_users(user_to_delete)

        if deleted:
            st.success(f"Deleted user '{user_to_delete}'.")
        else:
            st.error("User not found.")

st.header("📊 Analytics & Visual Insights")

if df.empty:
    st.info("No data available for analytics.")
else:
   
    st.subheader("Overview Metrics")
    
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Total Users", len(df))

    with col2:
        avg_user_len = df["username"].str.len().mean()
        st.metric("Avg Username Length", f"{avg_user_len:.1f} chars")

    with col3:
        avg_pass_len = df["password"].str.len().mean()
        st.metric("Avg Password Hash Length", f"{avg_pass_len:.1f} chars")

    st.subheader("📌 Username Length Distribution")
    df["username_length"] = df["username"].str.len()
    user_len_counts = df["username_length"].value_counts().sort_index()
    st.bar_chart(user_len_counts)

    st.subheader("🔐 Password Hash Length Distribution")
    df["password_length"] = df["password"].str.len()
    pass_len_counts = df["password_length"].value_counts().sort_index()
    st.bar_chart(pass_len_counts)
