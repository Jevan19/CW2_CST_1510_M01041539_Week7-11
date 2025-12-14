import sqlite3

conn = sqlite3.connect("database/platform.db")
cur = conn.cursor()

# Cyber incidents
cur.execute("""
INSERT INTO cyber_incidents (incident_type, severity, status, description)
VALUES
('Phishing', 'High', 'Open', 'Suspicious email reported'),
('Malware', 'Medium', 'Resolved', 'Malware cleaned')
""")

# Datasets
cur.execute("""
INSERT INTO datasets_metadata (name, size_bytes, rows, source)
VALUES
('Employee Data', 204800, 1200, 'HR'),
('Logs', 1048576, 50000, 'IT')
""")

# IT tickets
cur.execute("""
INSERT INTO it_tickets (title, priority, status, assigned_to)
VALUES
('Printer issue', 'Low', 'Open', 'Alex'),
('Network outage', 'High', 'In Progress', 'Sam')
""")

conn.commit()
conn.close()

print("✅ Sample data inserted")


import sqlite3
import os

DB_PATH = os.path.join("database", "platform.db")

def main():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    # If no tickets yet, insert sample data
    cur.execute("SELECT COUNT(*) FROM it_tickets")
    count = cur.fetchone()[0]

    if count == 0:
        sample = [
            ("Printer issue", "Low", "Open", "Alex", "2025-12-01 10:00", None),
            ("Network outage", "High", "In Progress", "Sam", "2025-12-01 09:00", None),
            ("Account reset", "Medium", "Waiting for User", "Alex", "2025-12-01 08:00", None),
            ("VPN not working", "High", "Resolved", "Sam", "2025-11-30 10:00", "2025-12-01 10:00"),
            ("Laptop overheating", "Medium", "Resolved", "Riya", "2025-11-29 09:00", "2025-12-01 09:00"),
            ("Email access", "Low", "Waiting for User", "Riya", "2025-11-30 12:00", None),
        ]
        cur.executemany("""
            INSERT INTO it_tickets (title, priority, status, assigned_to, created_at, resolved_at)
            VALUES (?, ?, ?, ?, ?, ?)
        """, sample)

    conn.commit()
    conn.close()
    print("✅ Sample IT ticket data inserted")

if __name__ == "__main__":
    main()