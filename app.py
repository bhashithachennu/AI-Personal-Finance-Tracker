from datetime import date

import pandas as pd
import streamlit as st

from analysis import (
    get_balance,
    get_total_expenses,
    get_total_income,
)
from charts import create_category_chart, create_income_expense_chart
from database import add_transaction, get_transactions, initialize_database
from insights import generate_insights


st.set_page_config(page_title="AI Personal Finance Tracker", page_icon="💰")

# Make sure the local database and transactions table are ready.
initialize_database()

st.title("AI Personal Finance Tracker")
st.write("Track your income and expenses and get a simple overview of your finances.")

st.header("Add a transaction")

with st.form("transaction_form"):
    transaction_date = st.date_input("Date", value=date.today())
    transaction_type = st.selectbox(
        "Type",
        options=["income", "expense"],
        format_func=str.title,
    )
    category = st.text_input("Category")
    amount = st.number_input("Amount", min_value=0.01, step=0.01)
    description = st.text_input("Description (optional)")

    submitted = st.form_submit_button("Save transaction")

if submitted:
    if not category.strip():
        st.warning("Please enter a category.")
    else:
        add_transaction(
            transaction_date.isoformat(),
            transaction_type,
            category.strip(),
            amount,
            description.strip(),
        )
        st.success("Transaction saved.")

st.header("Financial overview")

income = get_total_income()
expenses = get_total_expenses()
balance = get_balance()

income_column, expenses_column, balance_column = st.columns(3)
income_column.metric("Total income", f"{income:,.2f}")
expenses_column.metric("Total expenses", f"{expenses:,.2f}")
balance_column.metric("Balance", f"{balance:,.2f}")

st.header("Charts")
category_chart_column, comparison_chart_column = st.columns(2)

with category_chart_column:
    st.subheader("Expenses by category")
    st.pyplot(create_category_chart())

with comparison_chart_column:
    st.subheader("Income and expenses")
    st.pyplot(create_income_expense_chart())

st.header("Spending insights")
for insight in generate_insights():
    st.write(f"- {insight}")

st.header("All transactions")
transactions = get_transactions()

if transactions:
    transaction_table = pd.DataFrame(transactions)
    transaction_table = transaction_table.rename(
        columns={
            "id": "ID",
            "date": "Date",
            "type": "Type",
            "category": "Category",
            "amount": "Amount",
            "description": "Description",
        }
    )
    st.dataframe(transaction_table, use_container_width=True)
else:
    st.info("No transactions yet. Add one using the form above.")
