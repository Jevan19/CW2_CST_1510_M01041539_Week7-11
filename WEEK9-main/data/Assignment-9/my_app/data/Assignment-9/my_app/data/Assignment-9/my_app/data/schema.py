from app.data.db import connect_database


def create_tables():
    """
    Create all database tables if they do not already exist.
    """
    conn = connect_database()
    cursor = conn.cursor()

    # Users table (authentication)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password_hash TEXT NOT NULL,
        role TEXT NOT NULL
    );
    """)

    # Cyber incidents table (security domain)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS cyber_incidents (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT,
        incident_type TEXT,
        severity TEXT,
        status TEXT,
        description TEXT,
        reported_by TEXT
    );
    """)

    # Datasets metadata table (data domain)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS datasets_metadata (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        dataset_name TEXT,
        source TEXT,
        records INTEGER,
        last_updated TEXT
    );
    """)

    # IT tickets table (IT domain)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS it_tickets (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        employee TEXT,
        issue TEXT,
        priority TEXT,
        status TEXT
    );
    """)

    conn.commit()
    conn.close()