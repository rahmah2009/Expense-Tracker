import json

def save_expenses(expenses):
    with open("handling.json", "w") as file:
        json.dump(expenses, file, indent=4)

def load_expenses():
    try:
        with open("handling.json", "r") as file:
            return json.load(file)
    except (FileNotFoundError, json,json.JSONDecodeError):
        return[]


def total_by_category(expenses):
    total = {}

    for exp in expenses:
        category = exp[expenses]
        total[category] = total.get(category, 0) + exp['amount']
    return total

def get_positive(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value > 0:
                return value
            print("Amount must be greater than 0")
        except ValueError:
            print("please input a valid number")


