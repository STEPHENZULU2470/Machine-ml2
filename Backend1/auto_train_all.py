"""
Auto IDS Trainer: Downloads, preprocesses, merges, and uploads multiple public intrusion datasets for real-time IDS retraining.

Requirements:
- pandas
- requests
- scikit-learn
- tqdm
- (optionally) wget or urllib

Run: python auto_train_all.py
"""
import os
import pandas as pd
import requests
from io import BytesIO, StringIO
from zipfile import ZipFile
from tqdm import tqdm
from flask_cors import CORS

BACKEND_URL = 'http://localhost:5000'  # Change if backend runs elsewhere
UPLOAD_ENDPOINT = f'{BACKEND_URL}/upload'
METRICS_ENDPOINT = f'{BACKEND_URL}/metrics'

DATA_DIR = 'auto_datasets'
os.makedirs(DATA_DIR, exist_ok=True)

# --- NSL-KDD ---
def download_nsl_kdd():
    url = 'https://raw.githubusercontent.com/defcom17/NSL_KDD/master/KDDTrain+.txt'
    print('Downloading NSL-KDD...')
    df = pd.read_csv(url, header=None)
    # Hardcoded NSL-KDD columns (41 features + Label)
    nsl_kdd_columns = [
        'duration', 'protocol_type', 'service', 'flag', 'src_bytes', 'dst_bytes', 'land', 'wrong_fragment', 'urgent',
        'hot', 'num_failed_logins', 'logged_in', 'num_compromised', 'root_shell', 'su_attempted', 'num_root',
        'num_file_creations', 'num_shells', 'num_access_files', 'num_outbound_cmds', 'is_host_login', 'is_guest_login',
        'count', 'srv_count', 'serror_rate', 'srv_serror_rate', 'rerror_rate', 'srv_rerror_rate', 'same_srv_rate',
        'diff_srv_rate', 'srv_diff_host_rate', 'dst_host_count', 'dst_host_srv_count', 'dst_host_same_srv_rate',
        'dst_host_diff_srv_rate', 'dst_host_same_src_port_rate', 'dst_host_srv_diff_host_rate', 'dst_host_serror_rate',
        'dst_host_srv_serror_rate', 'dst_host_rerror_rate', 'dst_host_srv_rerror_rate', 'Label'
    ]
    # Drop extra columns if present
    if df.shape[1] > len(nsl_kdd_columns):
        print(f'NSL-KDD: Dropping {df.shape[1] - len(nsl_kdd_columns)} extra columns.')
        df = df.iloc[:, :len(nsl_kdd_columns)]
    elif df.shape[1] < len(nsl_kdd_columns):
        for _ in range(len(nsl_kdd_columns) - df.shape[1]):
            df[df.shape[1]] = None
    df.columns = nsl_kdd_columns
    print(f'NSL-KDD shape after column fix: {df.shape}')
    # Map labels
    df['Label'] = df['Label'].apply(lambda x: 'Benign' if x == 'normal' else 'Malicious')
    df.to_csv(os.path.join(DATA_DIR, 'nsl_kdd.csv'), index=False)
    print('NSL-KDD processed.')
    return df

# --- CICIDS2017 (small sample for demo) ---
def download_cicids2017():
    # Use a small, public sample
    url = 'https://raw.githubusercontent.com/smilli/IDS-DataSets/master/CICIDS2017/Friday-WorkingHours-Morning.pcap_ISCX.csv'
    print('Downloading CICIDS2017 sample...')
    df = pd.read_csv(url, low_memory=False)
    # Map labels
    df['Label'] = df['Label'].apply(lambda x: 'Benign' if 'BENIGN' in str(x).upper() else 'Malicious')
    df = df.dropna(axis=1, how='all')
    df.to_csv(os.path.join(DATA_DIR, 'cicids2017.csv'), index=False)
    print('CICIDS2017 sample processed.')
    return df

# --- UNSW-NB15 ---
def download_unsw_nb15():
    # Use a preprocessed version for demo
    url = 'https://raw.githubusercontent.com/huynhhoc/UNSW-NB15/master/UNSW_NB15_training-set.csv'
    print('Downloading UNSW-NB15...')
    df = pd.read_csv(url)
    # Map labels (0: Benign, 1: Malicious)
    if 'label' in df.columns:
        df['Label'] = df['label'].apply(lambda x: 'Malicious' if x == 1 else 'Benign')
    elif 'Label' in df.columns:
        df['Label'] = df['Label'].apply(lambda x: 'Malicious' if x == 1 else 'Benign')
    else:
        raise Exception('No label column found in UNSW-NB15')
    df.to_csv(os.path.join(DATA_DIR, 'unsw_nb15.csv'), index=False)
    print('UNSW-NB15 processed.')
    return df

# --- Merge Datasets ---
def merge_datasets(dfs):
    print('Merging datasets...')
    # Find common columns
    common_cols = set(dfs[0].columns)
    for df in dfs[1:]:
        common_cols &= set(df.columns)
    common_cols = list(common_cols)
    # Keep only common columns
    dfs = [df[common_cols] for df in dfs]
    merged = pd.concat(dfs, ignore_index=True)
    merged.to_csv(os.path.join(DATA_DIR, 'merged.csv'), index=False)
    print(f'Merged dataset shape: {merged.shape}')
    return merged

# --- Upload and Retrain ---
def upload_and_retrain(csv_path):
    print(f'Uploading {csv_path} to backend...')
    with open(csv_path, 'rb') as f:
        files = {'file': (os.path.basename(csv_path), f, 'text/csv')}
        resp = requests.post(UPLOAD_ENDPOINT, files=files)
    print('Upload response:', resp.json())
    if resp.status_code == 200:
        print('Retraining triggered.')
    else:
        print('Upload failed.')

# --- Check Metrics ---
def print_metrics():
    print('Checking model metrics...')
    resp = requests.get(METRICS_ENDPOINT)
    print('Model metrics:', resp.json())

# --- Main script ---
if __name__ == '__main__':
    datasets = []
    # NSL-KDD
    try:
        nsl = download_nsl_kdd()
        datasets.append(nsl)
    except Exception as e:
        print(f'Warning: NSL-KDD download failed: {e}')
    # CICIDS2017
    try:
        cic = download_cicids2017()
        datasets.append(cic)
    except Exception as e:
        print(f'Warning: CICIDS2017 download failed: {e}')
    # UNSW-NB15
    try:
        unsw = download_unsw_nb15()
        datasets.append(unsw)
    except Exception as e:
        print(f'Warning: UNSW-NB15 download failed: {e}')
    if not datasets:
        print('No datasets available for training. Exiting.')
        exit(1)
    merged = merge_datasets(datasets)
    # Sample to 5,000 rows to fit under 10MB
    sample_size = 5000
    if len(merged) > sample_size:
        print(f'Sampling merged dataset to {sample_size} rows to fit under 10MB upload limit.')
        merged = merged.sample(n=sample_size, random_state=42)
    merged_path = os.path.join(DATA_DIR, 'merged.csv')
    merged.to_csv(merged_path, index=False)
    # Print file size
    file_size_mb = os.path.getsize(merged_path) / (1024 * 1024)
    print(f'Merged CSV file size: {file_size_mb:.2f} MB')
    upload_and_retrain(merged_path)
    print('Waiting for retraining to complete (please check backend logs)...')
    import time; time.sleep(10)
    print_metrics()

# To enable backend file logging, add this to backend/app.py:
# import logging
# logging.basicConfig(filename='backend.log', level=logging.INFO) 