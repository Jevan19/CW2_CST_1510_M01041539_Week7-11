from data.db import connect_database


def insert_incident(conn, date, incident_type, severity, status, description, reported_by):
    """
    Insert a new cyber incident into the database.
    """
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO cyber_incidents
        (date, incident_type, severity, status, description, reported_by)
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        (date, incident_type, severity, status, description, reported_by)
    )

    conn.commit()
    return cursor.lastrowid


def update_incident_status(conn, incident_id, new_status):
    """
    Update the status of an existing incident.
    """
    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE cyber_incidents
        SET status = ?
        WHERE id = ?
        """,
        (new_status, incident_id)
    )

    conn.commit()


def delete_incident(conn, incident_id):
    """
    Delete an incident from the database.
    """
    cursor = conn.cursor()

    cursor.execute(
        """
        DELETE FROM cyber_incidents
        WHERE id = ?
        """,
        (incident_id,)
    )

    conn.commit()

import pandas as pd

def get_incidents_by_type_count(conn):
    query = """
    SELECT severity AS type, COUNT(*) AS count
    FROM cyber_incidents
    GROUP BY severity
    """
    return pd.read_sql_query(query, conn)
