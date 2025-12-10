import sys
import os
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(PROJECT_ROOT)
from app.services.database_manager import DatabaseManager
from app.services.auth_manager import AuthManager 
import streamlit as st


st.set_page_config(page_title="Login / Register", page_icon=":key:", layout="centered")

# Initialize session state
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "username" not in st.session_state:
    st.session_state.username = None

if "role" not in st.session_state:
    st.session_state.role = None

if "users" not in st.session_state:
    st.session_state.users = {}

st.title(":closed_lock_with_key: Welcome")

# Already logged in
if st.session_state.logged_in:
    st.success(f"Already logged in as **{st.session_state.username}**.")
    if st.button("Go to dashboard", key="btn_dashboard"):
        st.switch_page("pages/Dashboard.py")
    st.stop()

db = DatabaseManager(os.path.join(PROJECT_ROOT, "DATA", "intelligence.db"))
auth = AuthManager()  # initialize authentication system

tab_login, tab_register = st.tabs(["Login", "Register"])

with tab_login:
    st.subheader("Login")

    login_username = st.text_input("Username", key="login_username")
    login_password = st.text_input("Password", type="password", key="login_password")

    if st.button("Log in", key="btn_login"):
        success, message = auth.login_user(login_username, login_password)

        if success:
            st.success(message)
            st.session_state.logged_in = True
            st.session_state.username = login_username

            st.switch_page("pages/Dashboard.py")
        else:
            st.error(message)

with tab_register:
    st.subheader("Register New Account")

    new_username = st.text_input("Choose a username", key="new_username")
    new_password = st.text_input("Choose a password", type="password", key="new_password")
    confirm_password = st.text_input("Confirm password", type="password", key="confirm_password")

    if st.button("Create Account", key="btn_register"):
        if not new_username or not new_password:
            st.warning("Please fill in all fields.")
        elif new_password != confirm_password:
            st.error("Passwords do not match.")
        else:
            success, message = auth.registers_user(new_username, new_password)

            if success:
                st.success(message)
                st.info("Tip: go to the Login tab and sign in with your new account.")
            else:
                st.error(message)
