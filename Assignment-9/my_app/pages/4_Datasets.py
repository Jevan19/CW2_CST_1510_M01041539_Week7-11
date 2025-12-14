import streamlit as st
import pandas as pd
from data.db import connect_database

st.set_page_config(page_title="Datasets", page_icon="📊", layout="wide")

# Guard: if not logged in, send user back
if "logged_in" not in st.session_state or not st.session_state.logged_in:
    st.error("You must be logged in to view this page.")
    if st.button("Go to login page"):
        st.switch_page("pages/Login.py")
    st.stop()

st.title("📊 Datasets Metadata")
st.success(f"Logged in as **{st.session_state.username}**")

conn = connect_database()
cursor = conn.cursor()

# Fetch all datasets metadata
cursor.execute("SELECT * FROM datasets_metadata")
columns = [description[0] for description in cursor.description]
data = cursor.fetchall()
conn.close()

if data:
    df = pd.DataFrame(data, columns=columns)
    
    st.metric("Total Datasets", len(df))
    st.divider()
    
    st.subheader("Datasets Metadata")
    st.dataframe(df, use_container_width=True)
else:
    st.warning("No datasets metadata found in database.")
