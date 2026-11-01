import random

import os

import datetime as dt

import expense_utils as eu

from report_utils import generate_report

from tabulate import tabulate


expenses = []

print("===================================")
print("       PERSONAL EXPENSE TRACKER")
print("===================================")


while True:

    print("\nEnter Expense Details")

    description = input("Enter description: ")

    category = input("Enter category (Food/Travel/Study/Bills/Other): ")

    amount = float(input("Enter amount: "))

    # Validate amount

    if eu.validate_expense(amount) == False:

        print("Invalid amount! Please enter positive amount.")

        continue

    # Enter date

    date = input("Enter date (YYYY-MM-DD, blank for today): ")

    if date == "":

        date = dt.datetime.now().strftime("%Y-%m-%d")

    else:

        try:

            dt.datetime.strptime(date, "%Y-%m-%d")

        except ValueError:

            print("Invalid date format!")

            continue

    # Generate reference ID

    reference_id = "EXP-" + str(random.randint(100000, 999999))

    # Check duplicate ID

    for expense in expenses:

        while reference_id == expense["reference_id"]:

            reference_id = "EXP-" + str(random.randint(100000, 999999))

    # Store expense

    expense = {

        "reference_id": reference_id,

        "date": date,

        "description": description,

        "category": category,

        "amount": round(amount, 2)

    }

    expenses.append(expense)

    print("\nExpense Added Successfully!")

    print("Reference ID:", reference_id)

    # Add more expenses

    choice = input("\nDo you want to add another expense? (yes/no): ")

    if choice.lower() != "yes":

        break


# Display all expenses

print("\n========== ALL EXPENSES ==========")

table_data = []

for expense in expenses:

    table_data.append([

        expense["reference_id"],

        expense["date"],

        expense["description"],

        expense["category"],

        expense["amount"]

    ])


print(tabulate(

    table_data,

    headers=["Reference ID", "Date", "Description", "Category", "Amount"],

    tablefmt="grid"

))


# Generate monthly report

generate_report(expenses)


# Use os module

folder_path = os.path.dirname(os.path.abspath(__file__))

report_path = os.path.join(folder_path, "monthly_report.txt")

print("\n========== FILE CHECK ==========")

if os.path.exists(report_path):

    print("Monthly report file already exists.")

else:

    print("Monthly report file does not exist yet.")


print("\nThank you for using Personal Expense Tracker!")