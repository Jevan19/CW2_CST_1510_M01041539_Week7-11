import streamlit as st
from services.database_manager import DatabaseManager
from models.dataset import Dataset

st.title("📊 Data Science Dashboard")

db = DatabaseManager("database/platform.db")
db.connect()

rows = db.fetch_all("""
    SELECT id, name, size_bytes, rows, source
    FROM datasets
""")

datasets = [
    Dataset(
        dataset_id=row[0],
        name=row[1],
        size_bytes=row[2],
        rows=row[3],
        source=row[4]
    )
    for row in rows
]

if not datasets:
    st.info("No datasets found.")
else:
    for dataset in datasets:
        st.write(dataset)