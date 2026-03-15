import json
import pandas as pd

def export_csv():

    with open("expenses.json") as f:
        data = json.load(f)

    df = pd.DataFrame(data)

    df.to_csv("expenses.csv", index=False)

    print("Export completed")