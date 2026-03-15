import json
from collections import defaultdict

def spending_insight():

    with open("expenses.json") as f:
        expenses = json.load(f)

    data = defaultdict(float)

    for e in expenses:
        data[e["category"]] += e["amount"]

    total = sum(data.values())

    for cat,val in data.items():

        if val/total > 0.4:
            print("You spend too much on",cat)