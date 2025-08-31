import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import joblib
import shap
import os

DATA_PATH = os.path.join("..", "auto_datasets", "merged.csv")  # Use relative path
MODEL_PATH = 'rf_model.joblib'
EXPLAINER_PATH = 'shap_explainer.joblib'
FEATURES_PATH = 'features.txt'

# Check if dataset exists
if not os.path.exists(DATA_PATH):
    print(f"Dataset not found: {DATA_PATH}")
    print("Please ensure the merged.csv file exists in the auto_datasets directory")
    exit(1)

print(f"Using dataset: {DATA_PATH}")

# Load data (quick sample: first 10,000 rows)
try:
    df = pd.read_csv(DATA_PATH, nrows=10000)
    print(f"Loaded dataset with {len(df)} rows and {len(df.columns)} columns")
except Exception as e:
    print(f"Error loading dataset: {e}")
    exit(1)

# Assume the last column is the label
y = df.iloc[:, -1]
X = df.iloc[:, :-1]

print(f"Features: {len(X.columns)}, Labels: {len(y.unique())}")

# Encode non-numeric columns
def encode_features(X):
    return pd.get_dummies(X)

X_encoded = encode_features(X)
print(f"Encoded features: {X_encoded.shape[1]}")

# Save feature names
with open(FEATURES_PATH, 'w') as f:
    f.write('\n'.join(X_encoded.columns))
print(f"Features saved to {FEATURES_PATH}")

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X_encoded, y, test_size=0.2, random_state=42)

# Train model
print("Training Random Forest model...")
clf = RandomForestClassifier(n_estimators=20, random_state=42)
clf.fit(X_train, y_train)

# Evaluate
y_pred = clf.predict(X_test)
print('Accuracy:', accuracy_score(y_test, y_pred))
print('Precision:', precision_score(y_test, y_pred, average='macro', zero_division=0))
print('Recall:', recall_score(y_test, y_pred, average='macro', zero_division=0))
print('F1:', f1_score(y_test, y_pred, average='macro', zero_division=0))

# Save model
joblib.dump(clf, MODEL_PATH)
print(f'Model saved to {MODEL_PATH}')

# SHAP explainer
print("Creating SHAP explainer...")
explainer = shap.TreeExplainer(clf)
joblib.dump(explainer, EXPLAINER_PATH)
print(f'SHAP explainer saved to {EXPLAINER_PATH}')

print('Model and explainer saved successfully.')