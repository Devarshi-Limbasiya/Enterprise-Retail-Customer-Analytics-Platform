import pandas as pd
import matplotlib.pyplot as plt

# Read dataset
df = pd.read_csv('../datasets/master_dataset.csv')

# Calculate CLV
clv = df.groupby('customer_key').agg({
    'sales_amount':'sum',
    'order_number':'nunique'
})

clv.columns = [
    'Total_Revenue',
    'Total_Orders'
]

clv['Average_Order_Value'] = (
    clv['Total_Revenue']
    /
    clv['Total_Orders']
)

clv['Customer_Lifetime_Value'] = (
    clv['Average_Order_Value']
    *
    clv['Total_Orders']
)

print("\nTop Customers:")
print(
    clv
    .sort_values(
        'Customer_Lifetime_Value',
        ascending=False
    )
    .head(10)
)

# Save dataset
clv.to_csv(
    '../datasets/clv_dataset.csv'
)

# Plot
top10 = (
    clv
    .sort_values(
        'Customer_Lifetime_Value',
        ascending=False
    )
    .head(10)
)

plt.figure(figsize=(10,6))

plt.bar(
    top10.index.astype(str),
    top10['Customer_Lifetime_Value']
)

plt.title(
    'Top 10 Customers by CLV'
)

plt.xlabel(
    'Customer'
)

plt.ylabel(
    'Customer Lifetime Value'
)

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig(
    '../images/clv_analysis.png'
)

plt.show()

print("\nclv_dataset.csv created!")
print("clv_analysis.png created!")