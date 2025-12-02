import streamlit as st
import pandas as pd
import numpy as np
from app.services.userservice import login_user
from app.data.users import get_one_user


st.set_page_config(page_title="Login / Register", page_icon=":key:", layout="centered")

if "users" not in st.session_state:
    st.session_state.users = {}

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "username" not in st.session_state:
    st.session_state.username = ""
st.title(":closed_lock_with_key: Welcome")

if st.session_state.logged_in:
    st.success(f"Already logged in as **{st.session_state.username}**.")
    if st.button("Go to dashboard"):
        st.switch_page("pages/1_Dashboard")
    st.stop()

tab_login, tab_register = st.tabs(["Login", "Register"])
with tab_login:
    st.subheader("Login")
    login_username = st.text_input("Username", key="login_username")
    login_password = st.text_input("Password", type="password", key="login_password")

    if st.button("Log in", type="primary"):
        success, message = login_user(login_username, login_password)

        if success:
            st.success(message)

            # Store session info
            st.session_state.logged_in = True
            st.session_state.username = login_username

            # OPTIONAL: store role or other fields
            user = get_one_user(login_username)
            st.session_state.role = user[3]  
            st.switch_page("pages/1_Dashboard.py")
        else:
            st.error("Invalid username or password")

with tab_register:
    st.subheader("Register")
    new_username = st.text_input("Choose a username", key="register_username")
    new_password = st.text_input("Choose a password", type="password", key="register_password")
    confirm_password = st.text_input("Confirm password", type="password", key="register_confirm")

    if st.button("Create account"):
        if not new_username or not new_password:
            st.warning("Please fill in all fields.")
        elif new_password != confirm_password:
            st.error("Passwords do not match.")
        elif new_username in st.session_state.users:
            st.error("Username already exists. Choose another one.")
        else:
            st.session_state.users[new_username] = new_password
            st.success("Account created! You can now log in from the Login tab.")
            st.info("Tip: go to the Login tab and sign in your new account.")