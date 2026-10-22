import matplotlib.pyplot as plt

from analysis import get_category_expenses, get_total_expenses, get_total_income


def create_category_chart():
    """Create a bar chart of expenses grouped by category."""
    category_expenses = get_category_expenses()
    figure, axis = plt.subplots()

    if category_expenses.empty:
        axis.text(
            0.5,
            0.5,
            "No expense data to display yet.",
            horizontalalignment="center",
            verticalalignment="center",
        )
        axis.set_axis_off()
    else:
        category_expenses.plot(kind="bar", ax=axis, color="steelblue")
        axis.set_title("Expenses by Category")
        axis.set_xlabel("Category")
        axis.set_ylabel("Amount")
        axis.tick_params(axis="x", labelrotation=45)
        figure.tight_layout()

    return figure


def create_income_expense_chart():
    """Create a bar chart comparing total income and total expenses."""
    income = get_total_income()
    expenses = get_total_expenses()

    figure, axis = plt.subplots()
    axis.bar(["Income", "Expenses"], [income, expenses], color=["seagreen", "indianred"])
    axis.set_title("Income vs Expenses")
    axis.set_ylabel("Amount")
    figure.tight_layout()

    return figure
