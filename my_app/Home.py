
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st

st.set_page_config(page_title="Home", layout="wide")

# Initialize session state
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

st.title("Welcome to the Student Dashboard")

if st.session_state.logged_in:
    st.success(f"Logged in as: {st.session_state.username}")
    st.page_link("pages/Dashboard.py", label="Go to Dashboard")
else:
    st.warning("You are not logged in.")
    st.page_link("pages/Login.py", label="Go to Login Page")
