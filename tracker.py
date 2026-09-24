import json


def save_expense(expenses):
    with open("expenses.json", "w") as file:
        json.dump(expenses, file, indent=4)


def load_expense():
    try:
        with open("expenses.json", "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def total_by_category(expenses):
    totals = {}
    for exp in expenses:
        category = exp["category"]
        totals[category] = totals.get(category, 0) + exp["amount"]
    return totals


def get_positive_amount(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value > 0:
                return value
            print("Amount must be greater than zero.")
        except ValueError:
            print("Please enter a valid number.")


def delete_expense(expenses):
    if not expenses:
        print("No expenses to delete.")
        return

    while expenses:
        print("\n--- Delete Expense ---")
        for i, exp in enumerate(expenses, 1):
            print(
                f"{i}. {exp['category']}: ${exp['amount']:.2f} ({exp.get('description', '')})"
            )

        choice = input("\nEnter number to delete (0 to cancel): ").strip()
        if choice == "0":
            break

        if choice.isdigit() and 1 <= int(choice) <= len(expenses):
            removed = expenses.pop(int(choice) - 1)
            save_expense(expenses)
            print(f"Removed {removed['category']} (${removed['amount']:.2f}).")
        else:
            print("Invalid number. Try again.")
            continue

        if input("Delete another? (y/n): ").strip().lower() != "y":
            break


def Tracker():
    expenses = load_expense()

    while True:
        print("\n--- EXPENSE TRACKER ---")
        print("1. Add Expense")
        print("2. View Total Expense")
        print("3. View spending by Category")
        print("4. View Expense History")
        print("5. Delete Expense")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            amount = get_positive_amount("Enter amount: ")
            category = input("Enter category: ").strip().title()
            description = input("Input your expense description: ").strip()
            expenses.append(
                {"amount": amount, "category": category, "description": description}
            )
            save_expense(expenses)
            print("Expense added successfully!")

        elif choice == "2":
            if not expenses:
                print("No expenses found.")
            else:
                total = sum(item["amount"] for item in expenses)
                print(f"\nTotal Expense: ${total:.2f}")

        elif choice == "3":
            if not expenses:
                print("No expenses found")

            else:
                print("\nSpending by Category")
                for category, total in total_by_category(expenses).items():
                    print(f"{category}: ${total:.2f}")

        elif choice == "4":
            if not expenses:
                print("\nNo expense history found.")
            else:
                print("\n--- Expense History ---")
                total = 0
                for index, exp in enumerate(expenses, 1):
                    print(
                        f"{index}. Category: {exp['category']} |  Description: {exp.get('description', '')} | Amount: ${exp['amount']:.2f}"
                    )
                    total += exp["amount"]
                print("-" * 25)
                print(f"Total Spent: ${total:.2f}")

        elif choice == "5":
            delete_expense(expenses)

        elif choice == "6":
            print("BYEBYE👋👋👋!")
            break

        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    Tracker()
