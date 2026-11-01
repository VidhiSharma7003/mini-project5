import math


def validate_expense(amount):

    if amount > 0:
        return True
    else:
        return False


def calculate_total(expenses):

    total = 0

    for expense in expenses:
        total = total + expense["amount"]

    return round(total, 2)


def calculate_category_total(expenses):

    category_total = {}

    for expense in expenses:

        category = expense["category"]
        amount = expense["amount"]

        if category in category_total:
            category_total[category] = category_total[category] + amount

        else:
            category_total[category] = amount

    return category_total