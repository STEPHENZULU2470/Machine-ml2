import pandas as pd
import os

# Check if the dataset directory exists, if not create it
dataset_dir = 'dataset'
if not os.path.exists(dataset_dir):
    os.makedirs(dataset_dir)
    print(f"Created directory: {dataset_dir}")

# Load the original data - check if file exists
input_path = os.path.join(dataset_dir, 'Test_data.csv')
if not os.path.exists(input_path):
    print(f"Input file not found: {input_path}")
    print("Please place your Test_data.csv file in the dataset/ directory")
    exit(1)

try:
    df = pd.read_csv(input_path)
    print(f"Loaded dataset with {len(df)} rows and {len(df.columns)} columns")
except Exception as e:
    print(f"Error loading dataset: {e}")
    exit(1)

# Add a Label column: 'Malicious' if src_bytes > 1000, else 'Benign'
if 'src_bytes' in df.columns:
    df['Label'] = df['src_bytes'].apply(lambda x: 'Malicious' if x > 1000 else 'Benign')
else:
    print("Warning: 'src_bytes' column not found. Using first numeric column for labeling.")
    numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns
    if len(numeric_cols) > 0:
        col = numeric_cols[0]
        df['Label'] = df[col].apply(lambda x: 'Malicious' if x > 1000 else 'Benign')
        print(f"Used column '{col}' for labeling")
    else:
        print("No numeric columns found. Cannot create labels.")
        exit(1)

# Save to a new file
output_path = os.path.join(dataset_dir, 'Test_data_labeled.csv')
df.to_csv(output_path, index=False)

print(f"Labeled data saved to {output_path}. Label distribution:")
print(df['Label'].value_counts()) 