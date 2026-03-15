import json
from collections import defaultdict

FILE = "expenses.json"

def monthly_report():

    with open(FILE,"r") as f:
        expenses = json.load(f)

    total = 0
    categories = defaultdict(float)

    for e in expenses:
        total += e["amount"]
        categories[e["category"]] += e["amount"]

    print("Total Spending:", total)

    if categories:
        highest = max(categories, key=categories.get)
        print("Highest Category:", highest)