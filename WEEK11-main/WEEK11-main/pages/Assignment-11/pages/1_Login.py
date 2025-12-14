import streamlit as st
from services.database_manager import DatabaseManager
from services.auth_manager import AuthManager

st.title("🔐 Login")

# Initialize DB + Auth
db = DatabaseManager("database/platform.db")
db.connect()
auth = AuthManager(db)

# Inputs
username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Login"):
    user = auth.login_user(username, password)

    if user is None:
        st.error("Invalid username or password")
    else:
        st.success(f"Welcome, {user.get_username()}!")

        # Store user session
        st.session_state["logged_in"] = True
        st.session_state["username"] = user.get_username()
        st.session_state["role"] = user.get_role()