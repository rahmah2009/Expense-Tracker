# import json

# F = "expenses.json"


# def load():
#   try:
#     return json.load(open(F))
#   except (FileNotFoundError, json.JSONDecodeError):
#     return []


# def save(d):
#   json.dump(d, open(F, "w"), indent=4)


# def Tracker():
#   exps = load()
#   while True:
#     c = input(
#         "\n--- EXPENSE TRACKER ---\n1. Add Expense\n2. View Total"
#         " Expense\n3. View spending by Category\n4. View Expense History\n5."
#         " Delete Expense\n6. Exit\nChoose an option: "
#     )
#     if c == "1":
#       try:
#         a = float(input("Enter amount: "))
#         if a <= 0:
#           print("Amount must be greater than zero.")
#           continue
#         exps.append({
#             "amount": a,
#             "category": input("Enter category: ").strip().title(),
#             "description": input("Input your expense description: ").strip(),
#         })
#         save(exps)
#         print("Expense added successfully!")
#       except ValueError:
#         print("Please enter a valid number.")
#     elif c == "2":
#       print(
#           f"\nTotal Expense: ${sum(i['amount'] for i in exps):.2f}"
#           if exps
#           else "\nNo expenses found."
#       )
#     elif c == "3":
#       if not exps:
#         print("No expenses found")
#       else:
#         print("\nSpending by Category")
#         t = {}
#         for i in exps:
#           t[i["category"]] = t.get(i["category"], 0) + i["amount"]
#         for k, v in t.items():
#           print(f"{k}: ${v:.2f}")
#     elif c == "4":
#       if not exps:
#         print("\nNo expense history found.")
#       else:
#         print("\n--- Expense History ---")
#         for n, e in enumerate(exps, 1):
#           print(
#               f"{n}. Category: {e['category']} | Description:"
#               f" {e.get('description', '')} | Amount: ${e['amount']:.2f}"
#           )
#         print("-" * 25 + f"\nTotal Spent: ${sum(i['amount'] for i in exps):.2f}")
#     elif c == "5":
#       if not exps:
#         print("No expenses to delete.")
#         continue
#       for n, e in enumerate(exps, 1):
#         print(f"{n}. {e['category']}: ${e['amount']:.2f} ({e.get('description', '')})")
#       idx = input("Enter number to delete (0 to cancel): ")
#       if idx.isdigit() and 1 <= int(idx) <= len(exps):
#         rem = exps.pop(int(idx) - 1)
#         save(exps)
#         print(f   "Removed {rem['category']} (${rem['amount']:.2f}).")
#       else:
#         print("Invalid number.")
#     elif c == "6":
#       print("BYEBYE👋👋👋!")
#       break
#     else:
#       print("Invalid choice, try again.")


# if __name__ == "__main__":
#   Tracker()


import json


def save_expense(expense):
    with open("expenses.json", "w") as file:
        return json.dump(expense, file, indent=4)


def load_expense():
    try:
        with open("expenses.json", "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def total_by_category(expense):
    totals = {}
    for exp in expense:
        category = exp["category"]
        totals[category] = totals.get(category, 0) + exp["amount"]
    return totals


def get_positive_amount(prompt):
    while True:
        try:
            val = float(input(prompt))
            if val > 0:
                return val
            print("Amount must be greater than 0")
        except ValueError:
            print("please input a valid number")


def delete_expense(expense):
    if not expense:
        print("No expense to delete")
        return
    while expense:
        print("\n Delete expense")
        for i, exp in enumerate(expense, 1):
            print(
                f"{i}. {exp['category']}: ${exp['amount']:.2f} ({exp.get('description', '')})"
            )

        choice = input("\nEnter number to delete(0 to cancel): ").strip()
        if choice == "0":
            break

        if choice.isdigit() and 1 <= int(choice) <= len(expense):
            removed = expense.pop(int(choice) - 1)
            save_expense(expense)
            print(f"Removed {removed['category']} (${removed['amount']:.2f})")

        else:
            print("invalid option. try again in the nearest future😂😂😂")

        if input("Delete another? (y/n): ").strip().lower() != "y":
            break


def Tracker():
    expense = load_expense()

    while True:
        print("\n Expense Tracker")
        print("1. Add Expense")
        print("2. View total expense")
        print("3. View spending by cateory")
        print("4. View Expense History")
        print("5. Delete Expense History")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            amount = get_positive_amount("Enter Amount: ")
            category = input("Enter category: ").strip().title()
            description = input("Input your expense description: ").strip()
            expense.append(
                {"amount": amount, "category": category, "description": description}
            )
            save_expense(expense)
            print("Expense added successfully.")

        elif choice == "2":
            if not expense:
                print("No expenses found")
            else:
                total = sum(item["amount"] for item in expense)
                print(f"\n Total Expenses: ${total:.2f}")

        elif choice == "3":
            if not expense:
                print("No expense found")
            else:
                print("\n spending by category")
                for category, total in total_by_category(expense).items():
                    print(f"{category}: ${total:.2f}")

        elif choice == "4":
            if not expense:
                print("\n No expense found")
            else:
                print("\n Expense history")
                total = 0
                for index, exp in enumerate(expense, 1):
                    print(
                        f"{index}. Category: {exp['category']} | Description: {exp.get('description', '')} | Amount: ${exp['amount']:.2f}"
                    )
                    total += exp["amount"]
                    print(f"Total Spent: ${total:.2f}")

        elif choice == "6":
            print("DEY GO")
            break

        elif choice == "5":
            delete_expense(expense)

        else:
            print("invalid choice")


if __name__ == "__main__":
    Tracker()

# # # Write a Python program that asks the user for 5 expenses and prints the largest expense.


# def expense():
#     expenses = []

#     for i in range(5):
#         amount = float(input(f"Enter expense: "))
#         expenses.append(amount)
#     largest_expenses = max(expenses)
#     print(f"The largest expense is: {largest_expenses}")


# expense()
