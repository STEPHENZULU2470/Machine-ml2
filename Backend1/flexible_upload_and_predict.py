import pandas as pd
import requests
import os
import time
import json

BACKEND_URL = "http://localhost:5000"
FEATURES_PATH = "features.txt"  # Use relative path
UPLOAD_PATH = "mapped_upload.csv"  # Use relative path

# Check if features file exists
if not os.path.exists(FEATURES_PATH):
    print(f"Features file not found: {FEATURES_PATH}")
    print("Please ensure the model has been trained and features.txt exists")
    exit(1)

# 1. Load model features
try:
    with open(FEATURES_PATH) as f:
        model_features = [line.strip() for line in f if line.strip()]
    print(f"Loaded {len(model_features)} model features")
except Exception as e:
    print(f"Error loading features: {e}")
    exit(1)

# 2. Load user dataset
user_csv = input("Enter the path to your dataset CSV (e.g., kaggle_data.csv): ").strip()
if not os.path.exists(user_csv):
    print(f"File not found: {user_csv}")
    exit(1)

try:
    df = pd.read_csv(user_csv)
    print(f"Loaded dataset with columns: {list(df.columns)}")
except Exception as e:
    print(f"Error loading dataset: {e}")
    exit(1)

# 3. Map columns
mapped = {}
for feat in model_features:
    if feat in df.columns:
        mapped[feat] = df[feat]
    else:
        print(f"Feature '{feat}' not found in your dataset.")
        col = input(f"Enter the column name to use for '{feat}' (or leave blank to fill with 0): ").strip()
        if col and col in df.columns:
            mapped[feat] = df[col]
        else:
            mapped[feat] = 0

mapped_df = pd.DataFrame(mapped)
print(f"Mapped DataFrame shape: {mapped_df.shape}")

# 4. Save mapped CSV
mapped_df.to_csv(UPLOAD_PATH, index=False)
print(f"Saved mapped dataset to {UPLOAD_PATH}")

# 5. Upload the mapped dataset
print("Uploading mapped dataset...")
try:
    with open(UPLOAD_PATH, 'rb') as f:
        files = {'file': f}
        upload_resp = requests.post(f"{BACKEND_URL}/upload", files=files)
        print("Upload response:", upload_resp.json())
except Exception as e:
    print(f"Error uploading file: {e}")
    exit(1)

# Wait for retraining/processing
print("Waiting for backend to process the file...")
time.sleep(5)

# 6. Trigger prediction on the uploaded dataset
print("Requesting predictions on uploaded dataset...")
try:
    predict_resp = requests.post(f"{BACKEND_URL}/predict_uploaded")
    pred_json = predict_resp.json()
    print("Prediction response:", pred_json)
    with open("prediction_results.json", "w", encoding="utf-8") as f:
        json.dump(pred_json, f, indent=2)
    print("Prediction results saved to prediction_results.json")
except Exception as e:
    print("Error getting predictions:", e)

# 7. Download the forensic log
print("Downloading forensic log...")
try:
    log_resp = requests.get(f"{BACKEND_URL}/forensic-log")
    log_data = log_resp.json()
    with open("forensic_log_report.json", "w", encoding="utf-8") as f:
        json.dump(log_data, f, indent=2)
    print("Forensic log saved to forensic_log_report.json")
except Exception as e:
    print(f"Error downloading forensic log: {e}") 