import json
import os

# ---------- DATA LOAD / RESET ----------
print("Expense Tracker Startup")

choice = input("Do you want to keep previous data? (y/n): ").lower()

if choice == "n":

    with open("expenses.json", "w") as f:
        json.dump([], f)

    if os.path.exists("budget.json"):
        with open("budget.json", "w") as f:
            json.dump({"limit": 0}, f)

    print("Previous data cleared.\n")

else:
    print("Previous data loaded.\n")


# ---------- IMPORT MODULES ----------
from expense_manager import add_expense, view_expenses, edit_expense, delete_expense, search_category
from expense_analytics import monthly_report
from expense_visualization import showchart
from budget import set_budget, check_budget
from export import export_csv
from insights import spending_insight


# ---------- MAIN MENU ----------
while True:

    print("\nExpense Tracker")
    print("1 Set Budget")
    print("2 Add Expense")
    print("3 View Expenses")
    print("4 Edit Expense")
    print("5 Delete Expense")
    print("6 Search Category")
    print("7 Monthly Report")
    print("8 Budget Status")
    print("9 Show Chart")
    print("10 Export CSV")
    print("11 Insights")
    print("0 Exit")

    choice = input("Choice: ")

    if choice == "1":
        limit = float(input("Enter monthly budget: "))
        set_budget(limit)

    elif choice == "2":
        a = float(input("Amount: "))
        c = input("Category: ")
        d = input("Description: ")
        add_expense(a, c, d)

    elif choice == "3":
        view_expenses()

    elif choice == "4":
        i = int(input("Expense ID: "))
        amt = float(input("New amount: "))
        edit_expense(i, amt)

    elif choice == "5":
        i = int(input("Expense ID: "))
        delete_expense(i)

    elif choice == "6":
        cat = input("Category: ")
        search_category(cat)

    elif choice == "7":
        monthly_report()

    elif choice == "8":
        check_budget()

    elif choice == "9":
        showchart()

    elif choice == "10":
        export_csv()

    elif choice == "11":
        spending_insight()

    elif choice == "0":
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Try again.")