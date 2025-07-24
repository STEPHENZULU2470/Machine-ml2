import joblib
import shap
import pandas as pd
import os

# Paths
MODEL_PATH = os.path.join(os.path.dirname(__file__), 'rf_model.joblib')
DATA_PATH = os.path.join(os.path.dirname(__file__), '../auto_datasets/merged.csv')
EXPLAINER_PATH = os.path.join(os.path.dirname(__file__), 'shap_explainer.joblib')

# Load model
print('Loading model from:', MODEL_PATH)
model = joblib.load(MODEL_PATH)

# Load data (sample for speed)
print('Loading data from:', DATA_PATH)
data = pd.read_csv(DATA_PATH)
if 'label' in data.columns:
    X = data.drop('label', axis=1)
else:
    X = data

# Use a sample for SHAP to avoid memory issues
X_sample = X.sample(n=min(1000, len(X)), random_state=42)

# Create SHAP explainer
print('Creating SHAP explainer...')
explainer = shap.TreeExplainer(model)

# Save explainer
print('Saving explainer to:', EXPLAINER_PATH)
joblib.dump(explainer, EXPLAINER_PATH)
print('Done!') 