import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import joblib
import shap
import os

DATA_PATH = '../auto_datasets/merged.csv'  # Changed from Test_data_labeled.csv to merged dataset
MODEL_PATH = 'rf_model.joblib'
EXPLAINER_PATH = 'shap_explainer.joblib'
FEATURES_PATH = 'features.txt'

# Load data (quick sample: first 10,000 rows)
df = pd.read_csv(DATA_PATH, nrows=10000)

# Assume the last column is the label
y = df.iloc[:, -1]
X = df.iloc[:, :-1]

# Encode non-numeric columns
def encode_features(X):
    return pd.get_dummies(X)

X_encoded = encode_features(X)

# Save feature names
with open(FEATURES_PATH, 'w') as f:
    f.write('\n'.join(X_encoded.columns))

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X_encoded, y, test_size=0.2, random_state=42)

# Train model
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

# SHAP explainer
explainer = shap.TreeExplainer(clf)
joblib.dump(explainer, EXPLAINER_PATH)

print('Model and explainer saved.')