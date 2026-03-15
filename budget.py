import json

BUDGET_FILE = "budget.json"
EXPENSE_FILE = "expenses.json"


def set_budget(limit):

    data = {"limit": limit}

    with open(BUDGET_FILE, "w") as f:
        json.dump(data, f, indent=4)

    print("Budget set successfully!")


def check_budget():

    with open(BUDGET_FILE) as f:
        budget_data = json.load(f)

    limit = budget_data["limit"]

    with open(EXPENSE_FILE) as f:
        expenses = json.load(f)

    total = sum(e["amount"] for e in expenses)

    remaining = limit - total

    print("Budget Limit:", limit)
    print("Total Expenses:", total)
    print("Remaining Budget:", remaining)

    if remaining < 0:
        print("ALERT: Budget exceeded by", abs(remaining))

    elif total > limit * 0.8:
        print("Warning: Budget almost reached")

    else:
        print("Budget safe")