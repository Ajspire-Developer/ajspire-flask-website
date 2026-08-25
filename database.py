import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "instance" / "ajspire.db"


def get_connection():
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    return connection


def init_db():
    connection = get_connection()
    connection.execute("""
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            phone TEXT,
            message TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    connection.commit()
    connection.close()


def add_contact(name, email, phone, message):
    connection = get_connection()
    connection.execute(
        """
        INSERT INTO contacts (name, email, phone, message)
        VALUES (?, ?, ?, ?)
        """,
        (name, email, phone, message)
    )
    connection.commit()
    connection.close()


def get_contacts():
    connection = get_connection()
    contacts = connection.execute(
        "SELECT * FROM contacts ORDER BY id DESC"
    ).fetchall()
    connection.close()
    return contacts
