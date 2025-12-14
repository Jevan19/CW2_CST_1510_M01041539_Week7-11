from app.data.db import connect_database


def insert_ticket(employee, issue, priority, status):
    """
    Insert a new IT support ticket.
    """
    conn = connect_database()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO it_tickets
        (employee, issue, priority, status)
        VALUES (?, ?, ?, ?)
        """,
        (employee, issue, priority, status)
    )

    conn.commit()
    conn.close()


def get_all_tickets():
    """
    Retrieve all IT support tickets.
    """
    conn = connect_database()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM it_tickets")
    rows = cursor.fetchall()

    conn.close()
    return rows
