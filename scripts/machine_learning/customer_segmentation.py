import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# ======================================
# STEP 1: Load RFM Dataset
# ======================================

print("Loading RFM dataset...")

rfm = pd.read_csv('../datasets/rfm_dataset.csv')

print("\nDataset Shape:")
print(rfm.shape)

print("\nMissing Values:")
print(rfm.isnull().sum())

# ======================================
# STEP 2: Remove Missing Values
# ======================================

rfm = rfm.dropna(
    subset=['Recency', 'Frequency', 'Monetary']
)

print("\nDataset Shape After Cleaning:")
print(rfm.shape)

# ======================================
# STEP 3: Prepare Features
# ======================================

X = rfm[['Recency', 'Frequency', 'Monetary']]

# Scale features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# ======================================
# STEP 4: Train K-Means Model
# ======================================

kmeans = KMeans(
    n_clusters=4,
    random_state=42,
    n_init=10
)

rfm['Cluster'] = kmeans.fit_predict(X_scaled)

# ======================================
# STEP 5: Results
# ======================================

print("\nCluster Distribution:")
print(rfm['Cluster'].value_counts())

print("\nCluster Centers:")
print(kmeans.cluster_centers_)

# ======================================
# STEP 6: Save Results
# ======================================

rfm.to_csv(
    '../datasets/customer_segments_ml.csv',
    index=False
)

print("\ncustomer_segments_ml.csv created!")

# ======================================
# STEP 7: Visualization
# ======================================

plt.figure(figsize=(10,6))

scatter = plt.scatter(
    rfm['Frequency'],
    rfm['Monetary'],
    c=rfm['Cluster']
)

plt.title('K-Means Customer Segmentation')
plt.xlabel('Frequency')
plt.ylabel('Monetary')

plt.colorbar(scatter)

plt.tight_layout()

plt.savefig(
    '../images/kmeans_segmentation.png',
    dpi=300
)

plt.show()

print("kmeans_segmentation.png created!")