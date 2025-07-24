import requests
import time
import os

BACKEND_URL = "http://localhost:5000"
DATASET_PATH = os.path.join("auto_datasets", "merged.csv")  # Change if you want a different dataset

# 1. Upload the dataset
print("Uploading dataset...")
with open(DATASET_PATH, 'rb') as f:
    files = {'file': f}
    upload_resp = requests.post(f"{BACKEND_URL}/upload", files=files)
    print("Upload response:", upload_resp.json())

# Wait a bit for retraining/processing if needed
print("Waiting for backend to process the file...")
time.sleep(5)

# 2. Trigger prediction on the uploaded dataset
print("Requesting predictions on uploaded dataset...")
predict_resp = requests.post(f"{BACKEND_URL}/predict_uploaded")
print("Prediction response:", predict_resp.json())

# 3. Download the forensic log
print("Downloading forensic log...")
log_resp = requests.get(f"{BACKEND_URL}/forensic-log")
log_data = log_resp.json()
print(f"Forensic log entries: {len(log_data.get('log', []))}")

# Optionally, save the forensic log to a file for your report
with open("forensic_log_report.json", "w", encoding="utf-8") as f:
    import json
    json.dump(log_data, f, indent=2)
print("Forensic log saved to forensic_log_report.json") 