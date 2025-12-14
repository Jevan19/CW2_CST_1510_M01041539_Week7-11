import streamlit as st
from services.database_manager import DatabaseManager
from models.security_incident import SecurityIncident

st.title("🛡 Cybersecurity Dashboard")

db = DatabaseManager("database/platform.db")

try:
    rows = db.fetch_all("""
        SELECT id, incident_type, severity, status, description
        FROM security_incidents
    """)
except Exception as e:
    st.error("Database not initialised. Run db_setup.py once.")
    st.stop()

incidents = [
    SecurityIncident(*row) for row in rows
]

st.subheader("Incidents")

for incident in incidents:
    st.write(incident)

st.subheader("Severity Overview")

severity_counts = {"Low": 0, "Medium": 0, "High": 0, "Critical": 0}

for incident in incidents:
    sev = incident.get_severity().capitalize()
    if sev in severity_counts:
        severity_counts[sev] += 1

st.bar_chart(severity_counts)