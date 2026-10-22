import sqlite3
from pathlib import Path


# Keep the database file in the same folder as this Python file.
DATABASE_PATH = Path(__file__).with_name("finance.db")


def initialize_database():
    """Create the local database and transactions table if they do not exist."""
    connection = sqlite3.connect(DATABASE_PATH)

    try:
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS transactions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date TEXT NOT NULL,
                type TEXT NOT NULL,
                category TEXT NOT NULL,
                amount REAL NOT NULL,
                description TEXT
            )
            """
        )
        connection.commit()
    finally:
        connection.close()


def add_transaction(date, transaction_type, category, amount, description=""):
    """Save one income or expense transaction in the database."""
    connection = sqlite3.connect(DATABASE_PATH)

    try:
        connection.execute(
            """
            INSERT INTO transactions (date, type, category, amount, description)
            VALUES (?, ?, ?, ?, ?)
            """,
            (date, transaction_type, category, amount, description),
        )
        connection.commit()
    finally:
        connection.close()


def get_transactions():
    """Return all transactions as a list of dictionaries."""
    connection = sqlite3.connect(DATABASE_PATH)
    connection.row_factory = sqlite3.Row

    try:
        rows = connection.execute(
            """
            SELECT id, date, type, category, amount, description
            FROM transactions
            ORDER BY date DESC, id DESC
            """
        ).fetchall()
        return [dict(row) for row in rows]
    finally:
        connection.close()
