import bcrypt
from app.data.db import connect_database


def register_user(username, password, role="user"):
    """
    Register a new user in the database.
    """
    conn = connect_database()
    cursor = conn.cursor()

    # Hash the password
    hashed_password = bcrypt.hashpw(
        password.encode("utf-8"),
        bcrypt.gensalt()
    ).decode("utf-8")

    try:
        cursor.execute(
            """
            INSERT INTO users (username, password_hash, role)
            VALUES (?, ?, ?)
            """,
            (username, hashed_password, role)
        )
        conn.commit()
        conn.close()
        return True, "User registered successfully"

    except Exception as e:
        conn.close()
        return False, str(e)


def login_user(username, password):
    """
    Authenticate a user using username and password.
    """
    conn = connect_database()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT password_hash FROM users WHERE username = ?",
        (username,)
    )

    row = cursor.fetchone()
    conn.close()

    if row is None:
        return False, "User not found"

    stored_hash = row[0]

    if bcrypt.checkpw(password.encode("utf-8"), stored_hash.encode("utf-8")):
        return True, "Login successful"
    else:
        return False, "Incorrect password"