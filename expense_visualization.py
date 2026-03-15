import json
import matplotlib.pyplot as plt
from collections import defaultdict

def showchart():

    with open("expenses.json") as f:
        expenses = json.load(f)

    data = defaultdict(float)

    for e in expenses:
        data[e["category"]] += e["amount"]

    plt.pie(data.values(), labels=data.keys(), autopct="%1.1f%%")
    plt.title("Expense Distribution")
    plt.show()