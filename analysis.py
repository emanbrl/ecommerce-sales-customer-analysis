import pandas as pd

# Load the data
df = pd.read_excel("OnlineRetail.xlsx")

"""

# Inspecting the data 
print(df.head(5))
print(df.shape)
print(df.columns)
print(df.describe())
print(df.info())
print(df.isna().sum())
print(df[df["Quantity"] < 0].head())
"""


print(df["InvoiceNo"].astype(str).str.startswith("C").sum())
print(df[df["InvoiceNo"].astype(str).str.startswith("C")]["Quantity"].describe())