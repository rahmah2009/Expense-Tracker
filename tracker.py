def Tracker():
    expenses = []

    while True:
        print("\n--- EXPENSE TRACKER ---")
        print("1. Add Expense")
        print("2. View Total Expense")
        print("3. View Expense History")
        print("4. Delete Expense")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            amount = float(input("Enter amount: "))
            category = input("Enter category: ")
            expenses.append({"amount": amount, "category": category})
            print("Expense added successfully!")

        elif choice == "2":
            if not expenses:
                print("No expenses found.")
            else:
                total = sum(item['amount'] for item in expenses)
                print(f"\nTotal Expense: ${total:.2f}")

        elif choice == "3":
            if not expenses:
                print("\nNo expense history found.")
            else:
                print("\n--- Expense History ---")
                total = 0
                for index, exp in enumerate(expenses, 1):
                    print(f"{index}. Category: {exp['category']} | Amount: ${exp['amount']:.2f}")
                    total += exp["amount"]
                print("-" * 25)
                print(f"Total Spent: ${total:.2f}")            

        elif choice == "4":
            if not expenses:
                print("No expenses to delete.")
                continue

            print("\nSelect an item to delete:")
            for index, expense in enumerate(expenses, 1):
                print(f"{index}. Category: {expense['category']} - Amount: ${expense['amount']:.2f}")

            to_delete = int(input("Enter the number of the item to delete: ")) - 1

            if 0 <= to_delete < len(expenses):
                removed = expenses.pop(to_delete)
                print(f"Removed {removed['category']} expense of ${removed['amount']:.2f}")
            else:
                print("Invalid item number.")

        elif choice == "5":
            print("BYEBYE!")
            break

        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    Tracker()