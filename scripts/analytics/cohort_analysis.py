import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ======================================
# STEP 1: Load Dataset
# ======================================

print("Loading dataset...")

df = pd.read_csv('../datasets/master_dataset.csv')

df['order_date'] = pd.to_datetime(df['order_date'])

print("Dataset loaded!")
print("Shape:", df.shape)

# ======================================
# STEP 2: Create Cohorts
# ======================================

# Purchase month
df['OrderMonth'] = df['order_date'].dt.to_period('M')

# Customer first purchase month
df['CohortMonth'] = (
    df.groupby('customer_key')['OrderMonth']
    .transform('min')
)

# Calculate month difference
df['CohortIndex'] = (
    (df['OrderMonth'].dt.year - df['CohortMonth'].dt.year) * 12
    +
    (df['OrderMonth'].dt.month - df['CohortMonth'].dt.month)
    + 1
)

# ======================================
# STEP 3: Create Cohort Table
# ======================================

cohort_data = (
    df.groupby(['CohortMonth', 'CohortIndex'])['customer_key']
    .nunique()
    .reset_index()
)

cohort_table = cohort_data.pivot(
    index='CohortMonth',
    columns='CohortIndex',
    values='customer_key'
)

# ======================================
# STEP 4: Retention Matrix
# ======================================

cohort_sizes = cohort_table.iloc[:, 0]

retention = cohort_table.divide(
    cohort_sizes,
    axis=0
)

retention = retention.fillna(0)

# ======================================
# STEP 5: Save Dataset
# ======================================

retention.to_csv(
    '../datasets/cohort_retention.csv'
)

print("\nRetention Table Shape:")
print(retention.shape)

print("\nFirst 10 rows:")
print(retention.head(10))

# ======================================
# STEP 6: Plot Heatmap
# ======================================

plt.figure(figsize=(16,8))

sns.heatmap(
    retention,
    annot=False,
    cmap='Blues',
    vmin=0,
    vmax=1
)

plt.title(
    'Customer Cohort Retention Analysis',
    fontsize=16
)

plt.xlabel(
    'Months Since First Purchase'
)

plt.ylabel(
    'Customer Cohort'
)

plt.tight_layout()

plt.savefig(
    '../images/cohort_analysis.png',
    dpi=300
)

plt.show()

print("\ncohort_retention.csv created!")
print("cohort_analysis.png created!")