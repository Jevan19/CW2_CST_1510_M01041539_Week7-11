import sqlite3

DB_PATH = "database/platform.db"

def setup_database():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS security_incidents (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        incident_type TEXT,
        severity TEXT,
        status TEXT,
        description TEXT
    )
    """)

    cur.execute("SELECT COUNT(*) FROM security_incidents")
    count = cur.fetchone()[0]

    if count == 0:
        cur.executemany("""
        INSERT INTO security_incidents 
        (incident_type, severity, status, description)
        VALUES (?, ?, ?, ?)
        """, [
            ("Phishing", "high", "open", "Email phishing attack detected"),
            ("Malware", "critical", "open", "Malware found on server"),
            ("DDoS", "medium", "resolved", "Traffic spike detected"),
            ("Unauthorized Access", "low", "open", "Suspicious login attempt")
        ])

    conn.commit()
    conn.close()

if __name__ == "__main__":
    setup_database()
    print("Database ready.")