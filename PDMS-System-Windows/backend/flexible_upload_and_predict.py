import pandas as pd
import requests
import os
import time
import json

BACKEND_URL = "http://localhost:5000"
FEATURES_PATH = os.path.join("backend", "features.txt")
UPLOAD_PATH = os.path.join("backend", "mapped_upload.csv")

# 1. Load model features
with open(FEATURES_PATH) as f:
    model_features = [line.strip() for line in f if line.strip()]

# 2. Load user dataset
user_csv = input("Enter the path to your dataset CSV (e.g., kaggle_data.csv): ").strip()
df = pd.read_csv(user_csv)
print(f"Loaded dataset with columns: {list(df.columns)}")

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
with open(UPLOAD_PATH, 'rb') as f:
    files = {'file': f}
    upload_resp = requests.post(f"{BACKEND_URL}/upload", files=files)
    print("Upload response:", upload_resp.json())

# Wait for retraining/processing
print("Waiting for backend to process the file...")
time.sleep(5)

# 6. Trigger prediction on the uploaded dataset
print("Requesting predictions on uploaded dataset...")
predict_resp = requests.post(f"{BACKEND_URL}/predict_uploaded")
try:
    pred_json = predict_resp.json()
    print("Prediction response:", pred_json)
    with open("prediction_results.json", "w", encoding="utf-8") as f:
        json.dump(pred_json, f, indent=2)
    print("Prediction results saved to prediction_results.json")
except Exception as e:
    print("Error parsing prediction response:", e)

# 7. Download the forensic log
print("Downloading forensic log...")
log_resp = requests.get(f"{BACKEND_URL}/forensic-log")
log_data = log_resp.json()
with open("forensic_log_report.json", "w", encoding="utf-8") as f:
    json.dump(log_data, f, indent=2)
print("Forensic log saved to forensic_log_report.json") 