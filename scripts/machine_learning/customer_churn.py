import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)

# =====================================
# Load RFM dataset
# =====================================
print("Loading dataset...")

rfm = pd.read_csv('../datasets/rfm_scored.csv')

print("Dataset loaded!")
print("Shape:", rfm.shape)

# =====================================
# Create churn label
# Customers with high recency are
# considered churned
# =====================================
threshold = rfm['Recency'].quantile(0.75)

rfm['Churn'] = (
    rfm['Recency'] > threshold
).astype(int)

print("\nChurn Distribution:")
print(rfm['Churn'].value_counts())

# =====================================
# Features and Target
# =====================================
X = rfm[['Recency', 'Frequency', 'Monetary']]
y = rfm['Churn']

# =====================================
# Train/Test Split
# =====================================
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# =====================================
# Train Model
# =====================================
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

# =====================================
# Prediction
# =====================================
y_pred = model.predict(X_test)

# =====================================
# Evaluation
# =====================================
print("\nAccuracy:")
print(accuracy_score(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

print("\nConfusion Matrix:")
cm = confusion_matrix(y_test, y_pred)
print(cm)

# =====================================
# Feature Importance
# =====================================
importance = pd.DataFrame({
    'Feature': X.columns,
    'Importance': model.feature_importances_
})

importance = importance.sort_values(
    by='Importance',
    ascending=False
)

print("\nFeature Importance:")
print(importance)

# =====================================
# Plot Feature Importance
# =====================================
plt.figure(figsize=(8,5))

plt.bar(
    importance['Feature'],
    importance['Importance']
)

plt.title('Customer Churn Prediction')
plt.xlabel('Features')
plt.ylabel('Importance')

plt.savefig(
    '../images/customer_churn.png',
    dpi=300,
    bbox_inches='tight'
)

plt.show()

print("\ncustomer_churn.png created!")