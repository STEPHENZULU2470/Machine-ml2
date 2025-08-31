#!/bin/bash

echo "🚀 Starting IDS Backend System..."

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source venv/bin/activate

# Install/upgrade dependencies
echo "📚 Installing dependencies..."
pip install -r requirements.txt

# Create necessary directories
echo "📁 Creating necessary directories..."
mkdir -p dataset uploads

# Check if model files exist
if [ ! -f "rf_model.joblib" ] || [ ! -f "shap_explainer.joblib" ]; then
    echo "🤖 Training initial model..."
    python3 train_model.py
fi

# Check if tshark is installed
if ! command -v tshark &> /dev/null; then
    echo "⚠️  Warning: tshark not found. Packet capture features may not work."
    echo "   To install tshark: sudo apt install tshark"
fi

echo "✅ Setup complete! Starting Flask application..."
echo "🌐 The application will be available at http://localhost:5000"
echo "📊 API endpoints: /upload, /predict, /metrics, /history"

# Start the Flask application
python3 app.py