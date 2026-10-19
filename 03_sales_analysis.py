
import pandas as pd
from pathlib import Path

# Load cleaned data
file_path = "data/processed/cleaned_online_retail.csv"
df = pd.read_csv(file_path, parse_dates=["InvoiceDate"])

# Create output folder if it doesn't exist
output_folder = Path("data/processed")
output_folder.mkdir(parents=True, exist_ok=True)

# 1. Overall sales metrics
total_revenue = df["Revenue"].sum()
total_orders = df["InvoiceNo"].nunique()
total_customers = df["CustomerID"].nunique()
average_order_value = total_revenue / total_orders

print("\n--- OVERALL SALES METRICS ---")
print(f"Total Revenue: £{total_revenue:,.2f}")
print(f"Total Orders: {total_orders:,}")
print(f"Identified Customers: {total_customers:,}")
print(f"Average Order Value: £{average_order_value:,.2f}")

# 2. Monthly sales
df["Month"] = df["InvoiceDate"].dt.to_period("M").astype(str)

monthly_sales = (
    df.groupby("Month", as_index=False)["Revenue"]
    .sum()
    .sort_values("Month")
)

print("\n--- MONTHLY SALES ---")
print(monthly_sales.to_string(index=False))

monthly_sales.to_csv(
    output_folder / "monthly_sales.csv", index=False
)

# 3. Top 10 products by revenue
top_products = (
    df.groupby("Description", as_index=False)["Revenue"]
    .sum()
    .sort_values("Revenue", ascending=False)
    .head(10)
)

print("\n--- TOP 10 PRODUCTS BY REVENUE ---")
print(top_products.to_string(index=False))

top_products.to_csv(
    output_folder / "top_products.csv", index=False
)

# 4. Top 10 countries by revenue
country_sales = (
    df.groupby("Country", as_index=False)["Revenue"]
    .sum()
    .sort_values("Revenue", ascending=False)
    .head(10)
)

print("\n--- TOP 10 COUNTRIES BY REVENUE ---")
print(country_sales.to_string(index=False))

country_sales.to_csv(
    output_folder / "country_sales.csv", index=False
)

print("\nSales analysis completed successfully!")
print("Results saved in:", output_folder)
