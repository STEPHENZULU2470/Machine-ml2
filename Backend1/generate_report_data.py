import requests
import time
import os

BACKEND_URL = "http://localhost:5000"
DATASET_PATH = os.path.join("..", "auto_datasets", "merged.csv")  # Use relative path

# Check if dataset exists
if not os.path.exists(DATASET_PATH):
    print(f"Dataset not found: {DATASET_PATH}")
    print("Please ensure the merged.csv file exists in the auto_datasets directory")
    exit(1)

print(f"Using dataset: {DATASET_PATH}")

# 1. Upload the dataset
print("Uploading dataset...")
try:
    with open(DATASET_PATH, 'rb') as f:
        files = {'file': f}
        upload_resp = requests.post(f"{BACKEND_URL}/upload", files=files)
        print("Upload response:", upload_resp.json())
except Exception as e:
    print(f"Error uploading dataset: {e}")
    exit(1)

# Wait a bit for retraining/processing if needed
print("Waiting for backend to process the file...")
time.sleep(5)

# 2. Trigger prediction on the uploaded dataset
print("Requesting predictions on uploaded dataset...")
try:
    predict_resp = requests.post(f"{BACKEND_URL}/predict_uploaded")
    print("Prediction response:", predict_resp.json())
except Exception as e:
    print(f"Error getting predictions: {e}")

# 3. Download the forensic log
print("Downloading forensic log...")
try:
    log_resp = requests.get(f"{BACKEND_URL}/forensic-log")
    log_data = log_resp.json()
    print(f"Forensic log entries: {len(log_data.get('log', []))}")
    
    # Optionally, save the forensic log to a file for your report
    with open("forensic_log_report.json", "w", encoding="utf-8") as f:
        json.dump(log_data, f, indent=2)
    print("Forensic log saved to forensic_log_report.json")
except Exception as e:
    print(f"Error downloading forensic log: {e}") 