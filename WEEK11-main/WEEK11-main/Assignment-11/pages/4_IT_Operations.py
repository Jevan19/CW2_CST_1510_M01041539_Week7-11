import streamlit as st
from services.database_manager import DatabaseManager
from models.it_ticket import ITTicket

st.title("💻 IT Operations Dashboard")

db = DatabaseManager("database/platform.db")
db.connect()

rows = db.fetch_all("""
    SELECT id, title, priority, status, assigned_to
    FROM it_tickets
""")

tickets = [
    ITTicket(
        ticket_id=row[0],
        title=row[1],
        priority=row[2],
        status=row[3],
        assigned_to=row[4],
    )
    for row in rows
]

if not tickets:
    st.info("No IT tickets found.")
else:
    for ticket in tickets:
        st.write(ticket)