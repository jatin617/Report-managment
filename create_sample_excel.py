import pandas as pd

# Sample data dictionary
data = {
    "Date": ["2025-02-01", "2025-02-02", "2025-02-03"],
    "Product": ["Product A", "Product B", "Product C"],
    "Quantity": [10, 20, 30],
    "Sales": [1000, 2000, 3000]
}

# DataFrame create karo
df = pd.DataFrame(data)

# Excel file me data save karo (sample.xlsx)
df.to_excel("sample.xlsx", index=False)

print("sample.xlsx successfully created!")
