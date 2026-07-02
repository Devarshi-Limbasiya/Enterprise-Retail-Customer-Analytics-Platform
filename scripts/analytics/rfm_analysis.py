import pandas as pd
import matplotlib.pyplot as plt

# ======================================
# STEP 1: Load Dataset
# ======================================

print("Loading dataset...")

df = pd.read_csv('../datasets/master_dataset.csv')

df['order_date'] = pd.to_datetime(df['order_date'])

print("Dataset loaded!")
print("Shape:", df.shape)

# ======================================
# STEP 2: Calculate RFM
# ======================================

today = df['order_date'].max()

rfm = df.groupby('customer_key').agg({
    'order_date': lambda x: (today - x.max()).days,
    'order_number': 'nunique',
    'sales_amount': 'sum'
})

rfm.columns = [
    'Recency',
    'Frequency',
    'Monetary'
]

print("\nRFM Dataset:")
print(rfm.head())

# ======================================
# STEP 3: Create RFM Scores
# ======================================

# Recency
rfm['R_Score'] = pd.qcut(
    rfm['Recency'].rank(method='first'),
    q=5,
    labels=[5,4,3,2,1],
    duplicates='drop'
)

# Frequency
rfm['F_Score'] = pd.qcut(
    rfm['Frequency'].rank(method='first'),
    q=5,
    labels=[1,2,3,4,5],
    duplicates='drop'
)

# Monetary
rfm['M_Score'] = pd.qcut(
    rfm['Monetary'].rank(method='first'),
    q=5,
    labels=[1,2,3,4,5],
    duplicates='drop'
)

print("\nMissing Values Before Cleaning:")
print(
    rfm[['R_Score','F_Score','M_Score']]
    .isnull()
    .sum()
)

# Remove rows containing NaN scores
rfm = rfm.dropna(
    subset=['R_Score','F_Score','M_Score']
)

print("\nDataset Shape After Cleaning:")
print(rfm.shape)

# Convert scores to integer
rfm['R_Score'] = rfm['R_Score'].astype(int)
rfm['F_Score'] = rfm['F_Score'].astype(int)
rfm['M_Score'] = rfm['M_Score'].astype(int)

# ======================================
# STEP 4: Create RFM Score
# ======================================

rfm['RFM_Score'] = (
    rfm['R_Score'].astype(str)
    + rfm['F_Score'].astype(str)
    + rfm['M_Score'].astype(str)
)

# ======================================
# STEP 5: Customer Segmentation
# ======================================

def segment_customer(row):

    r = row['R_Score']
    f = row['F_Score']
    m = row['M_Score']

    if r >= 4 and f >= 4 and m >= 4:
        return "Champions"

    elif r >= 3 and f >= 3:
        return "Loyal Customers"

    elif r >= 4:
        return "Potential Loyalists"

    elif r == 3:
        return "Need Attention"

    elif r <= 2 and f >= 3:
        return "At Risk"

    else:
        return "Lost Customers"


rfm['Segment'] = rfm.apply(
    segment_customer,
    axis=1
)

print("\nCustomer Segments:")
print(rfm['Segment'].value_counts())

# ======================================
# STEP 6: Save Dataset
# ======================================

rfm.to_csv(
    '../datasets/rfm_segments.csv'
)

print("\nrfm_segments.csv created!")

# ======================================
# STEP 7: Visualization
# ======================================

segment_counts = rfm['Segment'].value_counts()

plt.figure(figsize=(10,6))

segment_counts.plot(
    kind='bar'
)

plt.title('Customer Segments')
plt.xlabel('Segment')
plt.ylabel('Number of Customers')

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig(
    '../images/rfm_segments.png'
)

plt.show()

print("\nrfm_segments.png created!")