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