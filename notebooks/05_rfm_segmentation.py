
import pandas as pd
from pathlib import Path

# Load cleaned data
df = pd.read_csv(
    "data/processed/cleaned_online_retail.csv",
    dtype={"InvoiceNo": str, "StockCode": str},
    parse_dates=["InvoiceDate"]
)

# Keep only records with customer IDs
df = df.dropna(subset=["CustomerID"]).copy()
df["CustomerID"] = df["CustomerID"].astype(int)

# Reference date for calculating recency
reference_date = df["InvoiceDate"].max() + pd.Timedelta(days=1)

# Calculate RFM metrics for each customer
rfm = df.groupby("CustomerID").agg(
    Recency=("InvoiceDate", lambda x: (reference_date - x.max()).days),
    Frequency=("InvoiceNo", "nunique"),
    Monetary=("Revenue", "sum")
).reset_index()

# Assign scores from 1 to 5
# Lower recency is better; higher frequency and spending are better
rfm["R_Score"] = pd.qcut(
    rfm["Recency"].rank(method="first"),
    5, labels=[5, 4, 3, 2, 1]
).astype(int)

rfm["F_Score"] = pd.qcut(
    rfm["Frequency"].rank(method="first"),
    5, labels=[1, 2, 3, 4, 5]
).astype(int)

rfm["M_Score"] = pd.qcut(
    rfm["Monetary"].rank(method="first"),
    5, labels=[1, 2, 3, 4, 5]
).astype(int)

# Combine scores
rfm["RFM_Score"] = (
    rfm["R_Score"].astype(str)
    + rfm["F_Score"].astype(str)
    + rfm["M_Score"].astype(str)
)

# Create customer segments
def assign_segment(row):
    if row["R_Score"] >= 4 and row["F_Score"] >= 4 and row["M_Score"] >= 4:
        return "Champions"
    elif row["R_Score"] >= 3 and row["F_Score"] >= 4:
        return "Loyal Customers"
    elif row["R_Score"] >= 4 and row["F_Score"] <= 2:
        return "Potential Loyalists"
    elif row["R_Score"] <= 2 and row["F_Score"] >= 3:
        return "At Risk"
    else:
        return "Other Customers"

rfm["Segment"] = rfm.apply(assign_segment, axis=1)

# Save results
output_path = Path("data/processed/rfm_customer_segments.csv")
output_path.parent.mkdir(parents=True, exist_ok=True)
rfm.to_csv(output_path, index=False)

# Display results
print("\n--- RFM CUSTOMER SEGMENTATION ---")
print("Total customers:", len(rfm))

print("\nCustomer segments:")
print(rfm["Segment"].value_counts().to_string())

print("\nTop 10 customers by RFM score:")
print(
    rfm.sort_values(
        ["R_Score", "F_Score", "M_Score"],
        ascending=False
    ).head(10).to_string(index=False)
)

print("\nRFM analysis completed successfully!")
print("Results saved to:", output_path)
