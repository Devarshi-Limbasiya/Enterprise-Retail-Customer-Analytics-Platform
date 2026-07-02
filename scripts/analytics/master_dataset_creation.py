import pyodbc
import pandas as pd

# Connect to SQL Server
conn = pyodbc.connect(
    "DRIVER={SQL Server};"
    "SERVER=DEVARSHI_PC\\SQLEXPRESS;"
    "DATABASE=DataWarehouse;"
    "Trusted_Connection=yes;"
)

print("Connected!")

# Create master dataset
query = """
SELECT
    fs.order_number,
    fs.order_date,
    fs.sales_amount,
    fs.quantity,
    fs.price,

    dc.customer_key,
    dc.customer_number,
    dc.first_name,
    dc.last_name,
    dc.country,

    dp.product_key,
    dp.product_name,
    dp.category,
    dp.subcategory,
    dp.cost

FROM gold.fact_sales fs
LEFT JOIN gold.dim_customers dc
    ON fs.customer_key = dc.customer_key

LEFT JOIN gold.dim_products dp
    ON fs.product_key = dp.product_key
"""

df = pd.read_sql(query, conn)

print("\nDataset Shape:")
print(df.shape)

print("\nFirst 5 Rows:")
print(df.head())

# Save dataset
df.to_csv("../datasets/master_dataset.csv", index=False)

print("\nmaster_dataset.csv created successfully!")
