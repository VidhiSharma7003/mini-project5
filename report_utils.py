import datetime as dt

from expense_utils import calculate_total
from expense_utils import calculate_category_total


def generate_report(expenses):

    current_month = dt.datetime.now().month
    current_year = dt.datetime.now().year

    monthly_expenses = []

    for expense in expenses:

        expense_date = dt.datetime.strptime(
            expense["date"], "%Y-%m-%d"
        )

        if expense_date.month == current_month and expense_date.year == current_year:

            monthly_expenses.append(expense)

    print("\n========== MONTHLY EXPENSE REPORT ==========")

    if len(monthly_expenses) == 0:

        print("No expenses found for this month.")

        return

    total = calculate_total(monthly_expenses)

    category_total = calculate_category_total(monthly_expenses)

    print("\nTotal Spending: Rs.", total)

    print("\nCategory Wise Expenses:")

    for category in category_total:

        print(category, ": Rs.", round(category_total[category], 2))

    print("\nReport Month:", dt.datetime.now().strftime("%B %Y"))