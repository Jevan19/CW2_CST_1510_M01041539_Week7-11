import sqlite3
import os

BASE_DIR = os.path.dirname(__file__)
DB_PATH = os.path.join(BASE_DIR, "intelligence_platform.db")

def connect_database():
    return sqlite3.connect(DB_PATH)