
import pandas as pd

# Load the raw dataset
file_path = "data/raw/Online Retail.xlsx"
df = pd.read_excel(file_path)

print("Original dataset shape:", df.shape)

# 1. Remove duplicate rows
df = df.drop_duplicates()

# 2. Remove rows with missing product descriptions
df = df.dropna(subset=["Description"])

# 3. Remove cancelled orders
df = df[~df["InvoiceNo"].astype(str).str.startswith("C")]

# 4. Remove invalid quantities and prices
df = df[(df["Quantity"] > 0) & (df["UnitPrice"] > 0)]

# 5. Create a revenue column
df["Revenue"] = df["Quantity"] * df["UnitPrice"]

# 6. Save the cleaned dataset
output_path = "data/processed/cleaned_online_retail.csv"
df.to_csv(output_path, index=False)

print("Cleaned dataset shape:", df.shape)
print("Missing values after cleaning:")
print(df.isnull().sum())
print("\nCleaned dataset saved to:", output_path)
