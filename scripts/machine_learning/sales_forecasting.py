import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# =====================================
# Load Dataset
# =====================================
print("Loading dataset...")

df = pd.read_csv('../datasets/master_dataset.csv')

# Convert order date
df['order_date'] = pd.to_datetime(df['order_date'])

print("Dataset loaded!")
print("Shape:", df.shape)

# =====================================
# Create Monthly Sales Dataset
# =====================================
monthly_sales = (
    df.groupby(df['order_date'].dt.to_period('M'))['sales_amount']
    .sum()
    .reset_index()
)

# Convert Period to Timestamp
monthly_sales['order_date'] = monthly_sales['order_date'].dt.to_timestamp()

# Remove incomplete last month
monthly_sales = monthly_sales.iloc[:-1]

print("\nMonthly Sales:")
print(monthly_sales.tail())

# =====================================
# Create Month Index
# =====================================
monthly_sales['Month'] = np.arange(
    1,
    len(monthly_sales) + 1
)

X = monthly_sales[['Month']]
y = monthly_sales['sales_amount']

# =====================================
# Train Model
# =====================================
model = LinearRegression()

model.fit(X, y)

# =====================================
# Forecast Next 12 Months
# =====================================
future_months = np.arange(
    len(monthly_sales) + 1,
    len(monthly_sales) + 13
).reshape(-1, 1)

forecast_sales = model.predict(future_months)

# =====================================
# Create Forecast Dataset
# =====================================
forecast_df = pd.DataFrame({
    'Month': future_months.flatten(),
    'Forecast_Sales': forecast_sales
})

forecast_df.to_csv(
    '../datasets/sales_forecast.csv',
    index=False
)

print("\nForecast Sales:")
print(forecast_df)

# =====================================
# Plot Forecast
# =====================================
plt.figure(figsize=(14,7))

# Historical Sales
plt.plot(
    monthly_sales['Month'],
    monthly_sales['sales_amount'],
    marker='o',
    linewidth=3,
    markersize=7,
    label='Historical Sales'
)

# Forecast line starts after historical data
plt.plot(
    forecast_df['Month'],
    forecast_df['Forecast_Sales'],
    marker='o',
    linestyle='--',
    linewidth=3,
    markersize=7,
    label='Forecast'
)

# Add vertical separator
plt.axvline(
    x=monthly_sales['Month'].max(),
    linestyle=':',
    linewidth=2
)

# Titles
plt.title(
    'Sales Forecasting',
    fontsize=24,
    fontweight='bold'
)

plt.xlabel(
    'Month',
    fontsize=16
)

plt.ylabel(
    'Sales',
    fontsize=16
)

plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

plt.legend(fontsize=14)
plt.grid(True, alpha=0.3)

plt.tight_layout()

# Save figure
plt.savefig(
    '../images/sales_forecasting.png',
    dpi=300,
    bbox_inches='tight'
)

plt.show()

print("\nFiles created successfully:")
print("✓ sales_forecast.csv")
print("✓ sales_forecasting.png")