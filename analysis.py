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


#print(df["InvoiceNo"].astype(str).str.startswith("C").sum())
#print(df[df["InvoiceNo"].astype(str).str.startswith("C")]["Quantity"].describe())
#print(df["InvoiceNo"].astype(str).str.startswith("C").value_counts())


"""
print(df.head(5))

print(df["UnitPrice"].describe())
print(df[df["UnitPrice"] <= 0].head(20))


# Country Column understanding so I get the "Is this retailer serving only the domestic UK market, or does it have international customers?" 
print(df["Country"].nunique())
print(df["Country"].unique())
print(df["Country"].value_counts())
"""

print(df["InvoiceNo"].astype(str).str.startswith("C"))