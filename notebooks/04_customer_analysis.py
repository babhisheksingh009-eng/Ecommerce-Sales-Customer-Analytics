
import pandas as pd
from pathlib import Path

# Load cleaned data
df = pd.read_csv(
    "data/processed/cleaned_online_retail.csv",
    dtype={"InvoiceNo": str, "StockCode": str},
    parse_dates=["InvoiceDate"]
)

# Keep only records with a known customer ID
customers = df.dropna(subset=["CustomerID"]).copy()
customers["CustomerID"] = customers["CustomerID"].astype(int)

# Create one row per customer
customer_summary = customers.groupby("CustomerID").agg(
    Total_Spending=("Revenue", "sum"),
    Total_Orders=("InvoiceNo", "nunique"),
    Total_Quantity=("Quantity", "sum"),
    Last_Purchase=("InvoiceDate", "max")
).reset_index()

# Average spending per order
customer_summary["Average_Order_Value"] = (
    customer_summary["Total_Spending"]
    / customer_summary["Total_Orders"]
)

# Days since the most recent purchase in the dataset
reference_date = df["InvoiceDate"].max() + pd.Timedelta(days=1)

customer_summary["Days_Since_Last_Purchase"] = (
    reference_date - customer_summary["Last_Purchase"]
).dt.days

# Repeat customer analysis
repeat_customers = (
    customer_summary["Total_Orders"] > 1
).sum()

total_customers = len(customer_summary)

repeat_rate = repeat_customers / total_customers * 100

print("\n--- CUSTOMER ANALYSIS ---")
print(f"Total identified customers: {total_customers:,}")
print(f"Repeat customers: {repeat_customers:,}")
print(f"Repeat purchase rate: {repeat_rate:.2f}%")

print("\n--- TOP 10 CUSTOMERS BY SPENDING ---")
top_customers = customer_summary.sort_values(
    "Total_Spending", ascending=False
).head(10)

print(top_customers.to_string(index=False))

# Save customer-level results
output_path = Path("data/processed/customer_summary.csv")
customer_summary.to_csv(output_path, index=False)

print("\nCustomer analysis completed successfully!")
print(f"Results saved to: {output_path}")
