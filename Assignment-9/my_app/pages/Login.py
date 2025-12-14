import streamlit as st

st.title("Login Page")

# Input field
username = st.text_input("Username")

# Login button
if st.button("Login"):
    if username.strip() == "":
        st.error("Please enter a username")
    else:
        st.session_state.logged_in = True
        st.session_state.username = username
        st.success("Logged in successfully!")
        st.switch_page("pages/1_Dashboard.py")