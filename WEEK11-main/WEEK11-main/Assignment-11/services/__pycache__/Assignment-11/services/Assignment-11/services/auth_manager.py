import hashlib
from models.user import User
from services.database_manager import DatabaseManager


class SimpleHasher:
    """Simple password hashing (demo only)."""

    @staticmethod
    def hash_password(password: str) -> str:
        return hashlib.sha256(password.encode()).hexdigest()

    @staticmethod
    def check_password(password: str, hashed: str) -> bool:
        return SimpleHasher.hash_password(password) == hashed


class AuthManager:
    """Handles authentication logic."""

    def __init__(self, db: DatabaseManager):
        self._db = db

    def login_user(self, username: str, password: str):
        row = self._db.fetch_one(
            "SELECT username, password_hash, role FROM users WHERE username = ?",
            (username,),
        )

        if row is None:
            return None

        username_db, password_hash_db, role_db = row

        if SimpleHasher.check_password(password, password_hash_db):
            return User(username_db, password_hash_db, role_db)

        return None