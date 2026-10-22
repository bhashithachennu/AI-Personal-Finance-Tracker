from analysis import (
    get_balance,
    get_category_expenses,
    get_total_expenses,
    get_total_income,
)


def generate_insights():
    """Return simple financial observations based on saved transactions."""
    insights = []

    category_expenses = get_category_expenses()
    if category_expenses.empty:
        insights.append("Add some expenses to see your highest-spending category.")
    else:
        highest_category = category_expenses.idxmax()
        highest_amount = category_expenses.max()
        insights.append(
            f"Your highest expense category is {highest_category} "
            f"at {highest_amount:.2f}."
        )

    income = get_total_income()
    expenses = get_total_expenses()
    if expenses > income:
        insights.append("Your expenses are higher than your income.")
    else:
        insights.append("Your expenses are not higher than your income.")

    balance = get_balance()
    if balance > 0:
        insights.append(f"Your current balance is positive at {balance:.2f}.")
    elif balance < 0:
        insights.append(f"Your current balance is negative at {balance:.2f}.")
    else:
        insights.append("Your current balance is zero.")

    return insights
