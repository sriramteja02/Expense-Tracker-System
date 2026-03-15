import json
from datetime import datetime

FILE = "expenses.json"

def load_expenses():
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except:
        return []

def save_expense(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)

def add_expense(amount, category, description):

    expenses = load_expenses()

    expense = {
        "id": len(expenses)+1,
        "amount": amount,
        "category": category,
        "description": description,
        "date": datetime.now().strftime("%Y-%m-%d")
    }

    expenses.append(expense)
    save_expense(expenses)

def view_expenses():

    expenses = load_expenses()

    for e in expenses:
        print(e)

def delete_expense(expense_id):

    expenses = load_expenses()
    expenses = [e for e in expenses if e["id"] != expense_id]

    save_expense(expenses)

def edit_expense(expense_id, new_amount):

    expenses = load_expenses()

    for e in expenses:
        if e["id"] == expense_id:
            e["amount"] = new_amount

    save_expense(expenses)

def search_category(category):

    expenses = load_expenses()

    for e in expenses:
        if e["category"] == category:
            print(e)