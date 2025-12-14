from app.data.schema import create_tables
from app.data.db import connect_database
from app.data.users import register_user, login_user
from app.data.incidents import (
    insert_incident,
    update_incident_status,
    delete_incident
)


def main():
    print("\n" + "=" * 50)
    print("WEEK 8 – DATABASE & CRUD TEST")
    print("=" * 50)

    # 1. Create database tables
    print("\n[STEP 1] Creating database tables...")
    create_tables()
    print("Tables created.")

    # 2. Test user registration
    print("\n[STEP 2] Testing user registration...")
    success, message = register_user("test_user", "TestPass123!")
    print("Register:", success, "-", message)

    # 3. Test login
    print("\n[STEP 3] Testing user login...")
    success, message = login_user("test_user", "TestPass123!")
    print("Login:", success, "-", message)

    # 4. Test incident CRUD
    print("\n[STEP 4] Testing incident CRUD...")
    conn = connect_database()

    incident_id = insert_incident(
        conn,
        "2024-12-12",
        "Test Incident",
        "Low",
        "Open",
        "This is a test incident",
        "test_user"
    )
    print(f"Incident created with ID: {incident_id}")

    update_incident_status(conn, incident_id, "Resolved")
    print("Incident status updated.")

    delete_incident(conn, incident_id)
    print("Incident deleted.")

    conn.close()

    print("\n" + "=" * 50)
    print("ALL TESTS COMPLETED SUCCESSFULLY")
    print("=" * 50)


if __name__ == "__main__":
    main()
