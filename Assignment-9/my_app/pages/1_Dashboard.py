import streamlit as st
import pandas as pd
import numpy as np
from data.db import connect_database
from data.incidents import get_incidents_by_type_count

st.set_page_config(page_title="Dashboard", page_icon="📊", layout="wide")

# Ensure state keys exist (in case user opens this page first)
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "username" not in st.session_state:
    st.session_state.username = ""

# Guard: if not logged in, send user back
if not st.session_state.logged_in:
    st.error("You must be logged in to view the dashboard.")
    if st.button("Go to login page"):
        st.switch_page("pages/Login.py")   # back to the first page
    st.stop()

# If logged in, show dashboard content
st.title("📊 Dashboard")
st.success(f"Hello, **{st.session_state.username}**! You are logged in.")

# Example dashboard layout
st.caption("This is just demo content – replace with your own dashboard.")

# Sidebar filters
with st.sidebar:
    st.header("Filters")
    n_points = st.slider("Number of data points", 10, 200, 50)

conn = connect_database()
df = get_incidents_by_type_count(conn)
conn.close()

st.subheader("Incidents by Type")
st.dataframe(df)


col1, col2 = st.columns(2)

with col1:
    st.subheader("Line chart")
    st.line_chart(df.set_index("type"))

with col2:
    st.subheader("Bar chart")
    st.bar_chart(df.set_index("type"))

with st.expander("See raw data"):
    st.dataframe(df.set_index("type"))

# Logout button
st.divider()
if st.button("Log out"):
    st.session_state.logged_in = False
    st.session_state.username = ""
    st.info("You have been logged out.")
    st.switch_page("Home.py")
