import streamlit as st
import pandas as pd
import plotly.express as px
from data.db import connect_database

st.set_page_config(page_title="Analytics", page_icon="📈", layout="wide")

# Guard: if not logged in, send user back
if "logged_in" not in st.session_state or not st.session_state.logged_in:
    st.error("You must be logged in to view this page.")
    if st.button("Go to login page"):
        st.switch_page("pages/Login.py")
    st.stop()

st.title("📈 Analytics & Charts")
st.success(f"Logged in as **{st.session_state.username}**")

conn = connect_database()

col1, col2 = st.columns(2)

with col1:
    st.subheader("Cyber Incidents by Severity")
    cursor = conn.cursor()
    cursor.execute("SELECT severity, COUNT(*) as count FROM cyber_incidents GROUP BY severity")
    incidents = pd.DataFrame(cursor.fetchall(), columns=['severity', 'count'])
    
    if not incidents.empty:
        fig_incidents = px.pie(incidents, values='count', names='severity', title='Incidents by Severity')
        st.plotly_chart(fig_incidents, use_container_width=True)
    else:
        st.warning("No incident data available")

with col2:
    st.subheader("IT Tickets by Priority")
    cursor = conn.cursor()
    cursor.execute("SELECT priority, COUNT(*) as count FROM it_tickets GROUP BY priority")
    tickets = pd.DataFrame(cursor.fetchall(), columns=['priority', 'count'])
    
    if not tickets.empty:
        fig_tickets = px.pie(tickets, values='count', names='priority', title='Tickets by Priority')
        st.plotly_chart(fig_tickets, use_container_width=True)
    else:
        st.warning("No ticket data available")

st.divider()

col3, col4 = st.columns(2)

with col3:
    st.subheader("Incident Status Distribution")
    cursor = conn.cursor()
    cursor.execute("SELECT status, COUNT(*) as count FROM cyber_incidents GROUP BY status")
    status_data = pd.DataFrame(cursor.fetchall(), columns=['status', 'count'])
    
    if not status_data.empty:
        fig_status = px.bar(status_data, x='status', y='count', title='Incidents by Status')
        st.plotly_chart(fig_status, use_container_width=True)

with col4:
    st.subheader("Ticket Status Distribution")
    cursor = conn.cursor()
    cursor.execute("SELECT status, COUNT(*) as count FROM it_tickets GROUP BY status")
    ticket_status = pd.DataFrame(cursor.fetchall(), columns=['status', 'count'])
    
    if not ticket_status.empty:
        fig_ticket_status = px.bar(ticket_status, x='status', y='count', title='Tickets by Status')
        st.plotly_chart(fig_ticket_status, use_container_width=True)

conn.close()
