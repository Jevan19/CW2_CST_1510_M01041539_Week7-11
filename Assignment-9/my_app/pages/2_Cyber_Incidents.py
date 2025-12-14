import streamlit as st
import pandas as pd
from data.db import connect_database

st.set_page_config(page_title="Cyber Incidents", page_icon="🛡️", layout="wide")

# Guard: if not logged in, send user back
if "logged_in" not in st.session_state or not st.session_state.logged_in:
    st.error("You must be logged in to view this page.")
    if st.button("Go to login page"):
        st.switch_page("pages/Login.py")
    st.stop()

st.title("🛡️ Cyber Incidents")
st.success(f"Logged in as **{st.session_state.username}**")

conn = connect_database()
cursor = conn.cursor()

# Fetch all cyber incidents
cursor.execute("SELECT * FROM cyber_incidents")
columns = [description[0] for description in cursor.description]
data = cursor.fetchall()
conn.close()

if data:
    df = pd.DataFrame(data, columns=columns)
    
    # Display stats
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Incidents", len(df))
    with col2:
        critical = len(df[df['severity'] == 'Critical'])
        st.metric("Critical", critical)
    with col3:
        high = len(df[df['severity'] == 'High'])
        st.metric("High", high)
    
    st.divider()
    
    # Filters
    with st.sidebar:
        st.header("Filters")
        severity_filter = st.multiselect("Severity", options=df['severity'].unique())
        status_filter = st.multiselect("Status", options=df['status'].unique())
    
    # Apply filters
    filtered_df = df.copy()
    if severity_filter:
        filtered_df = filtered_df[filtered_df['severity'].isin(severity_filter)]
    if status_filter:
        filtered_df = filtered_df[filtered_df['status'].isin(status_filter)]
    
    st.subheader(f"Incidents ({len(filtered_df)})")
    st.dataframe(filtered_df, use_container_width=True)
else:
    st.warning("No incidents found in database.")
