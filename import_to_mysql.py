
import pandas as pd
import mysql.connector

# Read the cleaned CSV file
file_path = "data/processed/cleaned_online_retail.csv"
df = pd.read_csv(file_path, dtype={"InvoiceNo": str, "StockCode": str})

# Replace missing values with None for MySQL
df = df.astype(object).where(pd.notna(df), None)

# Connect to MySQL
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password=input("Enter your MySQL root password: "),
    database="ecommerce_analytics"
)

cursor = connection.cursor()

# Insert data in batches
sql = """
INSERT INTO online_retail
(InvoiceNo, StockCode, Description, Quantity, InvoiceDate,
 UnitPrice, CustomerID, Country, Revenue)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
"""

batch_size = 5000

for start in range(0, len(df), batch_size):
    batch = df.iloc[start:start + batch_size]
    rows = [
        tuple(None if pd.isna(value) else value for value in row)
        for row in batch.itertuples(index=False, name=None)
    ]
    cursor.executemany(sql, rows)
    connection.commit()
    print(f"Imported {min(start + batch_size, len(df))} of {len(df)} rows")

cursor.close()
connection.close()

print("Import completed successfully!")
