import sqlite3

DB_PATH = "database/platform.db"

conn = sqlite3.connect(DB_PATH)
cur = conn.cursor()

# Users table
cur.execute("""
CREATE TABLE IF NOT EXISTS users (
    username TEXT PRIMARY KEY,
    password_hash TEXT,
    role TEXT
)
""")

# Cybersecurity incidents
cur.execute("""
CREATE TABLE IF NOT EXISTS cyber_incidents (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    incident_type TEXT,
    severity TEXT,
    status TEXT,
    description TEXT
)
""")

# Data science datasets
cur.execute("""
CREATE TABLE IF NOT EXISTS datasets_metadata (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    size_bytes INTEGER,
    rows INTEGER,
    source TEXT
)
""")

# IT tickets
cur.execute("""
CREATE TABLE IF NOT EXISTS it_tickets (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    priority TEXT,
    status TEXT,
    assigned_to TEXT
)
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS it_tickets (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    priority TEXT NOT NULL,
    status TEXT NOT NULL,
    assigned_to TEXT NOT NULL,
    created_at TEXT NOT NULL,
    resolved_at TEXT
);
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS datasets (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    size_bytes INTEGER NOT NULL,
    rows INTEGER NOT NULL,
    source TEXT NOT NULL
) ;
 """)           


conn.commit()
conn.close()

print("✅ Database schema created successfully")