import pyodbc
import pandas as pd

# Connect to SQL Server
conn = pyodbc.connect(
    "DRIVER={SQL Server};"
    "SERVER=DEVARSHI_PC\\SQLEXPRESS;"
    "DATABASE=DataWarehouse;"
    "Trusted_Connection=yes;"
)

print("✅ Connected to SQL Server!")

# Test query
query = """
SELECT TOP 5 *
FROM gold.fact_sales
"""

df = pd.read_sql(query, conn)

print("\nFirst 5 rows:")
print(df.head())

print("\nDataset Information:")
print(df.info())
