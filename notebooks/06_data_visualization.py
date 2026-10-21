
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Folder containing our analysis results
data_folder = Path("data/processed")
chart_folder = data_folder / "charts"
chart_folder.mkdir(parents=True, exist_ok=True)

# Load results from previous analysis steps
monthly_sales = pd.read_csv(data_folder / "monthly_sales.csv")
top_products = pd.read_csv(data_folder / "top_products.csv")
country_sales = pd.read_csv(data_folder / "country_sales.csv")
rfm = pd.read_csv(data_folder / "rfm_customer_segments.csv")

# -----------------------------------
# Chart 1: Monthly Sales Revenue
# -----------------------------------
plt.figure(figsize=(12, 6))
plt.plot(
    monthly_sales["Month"],
    monthly_sales["Revenue"],
    marker="o"
)
plt.title("Monthly Sales Revenue")
plt.xlabel("Month")
plt.ylabel("Revenue (£)")
plt.xticks(rotation=45)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig(chart_folder / "monthly_sales.png", dpi=300)
plt.close()

# -----------------------------------
# Chart 2: Top 10 Products by Revenue
# -----------------------------------
products = top_products.sort_values("Revenue")

plt.figure(figsize=(12, 7))
plt.barh(products["Description"], products["Revenue"])
plt.title("Top 10 Products by Revenue")
plt.xlabel("Revenue (£)")
plt.ylabel("Product")
plt.tight_layout()
plt.savefig(chart_folder / "top_products.png", dpi=300)
plt.close()

# -----------------------------------
# Chart 3: Top 10 Countries by Revenue
# -----------------------------------
countries = country_sales.sort_values("Revenue")

plt.figure(figsize=(10, 6))
plt.barh(countries["Country"], countries["Revenue"])
plt.title("Top 10 Countries by Revenue")
plt.xlabel("Revenue (£)")
plt.ylabel("Country")
plt.tight_layout()
plt.savefig(chart_folder / "country_sales.png", dpi=300)
plt.close()

# -----------------------------------
# Chart 4: Customer Segments
# -----------------------------------
segments = rfm["Segment"].value_counts().sort_values()

plt.figure(figsize=(10, 6))
plt.barh(segments.index, segments.values)
plt.title("Customer Segmentation (RFM Analysis)")
plt.xlabel("Number of Customers")
plt.ylabel("Customer Segment")
plt.tight_layout()
plt.savefig(chart_folder / "customer_segments.png", dpi=300)
plt.close()

print("All 4 charts created successfully!")
print("Charts saved in:", chart_folder.resolve())
