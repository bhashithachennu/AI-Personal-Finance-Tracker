import pandas as pd

from database import get_transactions, initialize_database


def _get_transactions_dataframe():
    """Load saved transactions into a Pandas DataFrame."""
    initialize_database()
    transactions = get_transactions()
    return pd.DataFrame(
        transactions,
        columns=["id", "date", "type", "category", "amount", "description"],
    )


def get_total_income():
    """Return the sum of all income transactions."""
    transactions = _get_transactions_dataframe()
    income = transactions[transactions["type"] == "income"]
    return income["amount"].sum()


def get_total_expenses():
    """Return the sum of all expense transactions."""
    transactions = _get_transactions_dataframe()
    expenses = transactions[transactions["type"] == "expense"]
    return expenses["amount"].sum()


def get_balance():
    """Return total income minus total expenses."""
    return get_total_income() - get_total_expenses()


def get_category_expenses():
    """Return expense totals grouped by category as a Pandas Series."""
    transactions = _get_transactions_dataframe()
    expenses = transactions[transactions["type"] == "expense"]
    return expenses.groupby("category")["amount"].sum().sort_values(ascending=False)
