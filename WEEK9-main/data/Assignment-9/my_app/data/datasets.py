from app.data.db import connect_database


def insert_dataset(dataset_name, source, records, last_updated):
    """
    Insert a dataset record into the database.
    """
    conn = connect_database()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO datasets_metadata
        (dataset_name, source, records, last_updated)
        VALUES (?, ?, ?, ?)
        """,
        (dataset_name, source, records, last_updated)
    )

    conn.commit()
    conn.close()


def get_all_datasets():
    """
    Retrieve all dataset records.
    """
    conn = connect_database()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM datasets_metadata")
    rows = cursor.fetchall()

    conn.close()
    return rows