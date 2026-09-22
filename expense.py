import json

def save_expenses(expenses):
    with open("expense.json", "w") as file:
        json.dump(expenses, file, indent=4)

def load_expenses():
    try:
        with open("expense.json", "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return[]

def total_by_category(expenses):
    total = {}
    for exp in expenses:
        category = exp["category"]
        total[category] = total.get(category, 0) + exp["amount"]
    return total

def get_positive_amount(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value > 0:
                return value
            print ("Amount must be greater than zero.")
        except ValueError:
            print("Enter a valid number")

# def delete_expenses(expenses):

def tracker():
    expenses = load_expenses()

    while True:
        print("\n ----------Expense_Tracker----------")
        print("1.Add expenses")
        print("2. view total expenses")
        print("3. View spending by category")
        print("4. view expense history")
        print("5. Exit")
        print("6. Delete")

        choice = input("Choose an option: ")


        if choice == "1":
            amount = get_positive_amount("Enter amount: ")
            category = input("Enter category: ").strip().title()
            description = input("Input your expense description: ").strip()
            expenses.append({"amount": amount, "category": category, "description": description})
            save_expenses(expenses)
            print("Expense added successfully")

        elif choice == "2":
            if not expenses:
                print("No expenses found")
            else:
                total = sum(item['amount' for item])

        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    tracker()