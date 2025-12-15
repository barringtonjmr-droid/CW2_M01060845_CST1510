import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

import streamlit as st
import pandas as pd
from database.db import connect_database
from app.data.users import (
    insert_data,
    update_users,
    delete_users,   
    get_all_users_pandas
)
conn = connect_database()
st.title("😄 Welcome to the User Management Dashboard")

# Protect Page
if "logged_in" not in st.session_state:
    st.error("You must log in first. Please go to the Login page from the sidebar.")
    st.stop()
st.image("services/Nice.jpg", caption="Domain Intelligence")

st.subheader("How it works")
st.write("""
This dashboard allows you to choose a specific domain, and provides CRUD operations and visualisations for each domain. Additionally, there is an AI Assistant to help you navigate and utilize the platform effectively.
""")                                    
st.subheader("Please choose an Domain")
if st.button("Cybersecurity Dashboard"):
    st.switch_page("pages/Cybersecurity.py")
if st.button("Datasets Dashboard"):
    st.switch_page("pages/Datasets.py")
if st.button("IT Operations Dashboard"):
    st.switch_page("pages/IT_Operations.py")
if st.button("AI Assistant"):
    st.switch_page("pages/AI_Assistant.py")
