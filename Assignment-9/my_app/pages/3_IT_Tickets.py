import streamlit as st
import pandas as pd
from data.db import connect_database

st.set_page_config(page_title="IT Tickets", page_icon="🎫", layout="wide")

# Guard: if not logged in, send user back
if "logged_in" not in st.session_state or not st.session_state.logged_in:
    st.error("You must be logged in to view this page.")
    if st.button("Go to login page"):
        st.switch_page("pages/Login.py")
    st.stop()

st.title("🎫 IT Tickets")
st.success(f"Logged in as **{st.session_state.username}**")

conn = connect_database()
cursor = conn.cursor()

# Fetch all IT tickets
cursor.execute("SELECT * FROM it_tickets")
columns = [description[0] for description in cursor.description]
data = cursor.fetchall()
conn.close()

if data:
    df = pd.DataFrame(data, columns=columns)
    
    # Display stats
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Tickets", len(df))
    with col2:
        open_tickets = len(df[df['status'] == 'Open'])
        st.metric("Open", open_tickets)
    with col3:
        closed_tickets = len(df[df['status'] == 'Closed'])
        st.metric("Closed", closed_tickets)
    
    st.divider()
    
    # Filters
    with st.sidebar:
        st.header("Filters")
        priority_filter = st.multiselect("Priority", options=df['priority'].unique())
        status_filter = st.multiselect("Status", options=df['status'].unique())
    
    # Apply filters
    filtered_df = df.copy()
    if priority_filter:
        filtered_df = filtered_df[filtered_df['priority'].isin(priority_filter)]
    if status_filter:
        filtered_df = filtered_df[filtered_df['status'].isin(status_filter)]
    
    st.subheader(f"Tickets ({len(filtered_df)})")
    st.dataframe(filtered_df, use_container_width=True)
else:
    st.warning("No tickets found in database.")
