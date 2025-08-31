#!/bin/bash

echo "🔧 PDMS - AI-Powered Intrusion Detection & Mitigation System"
echo "============================================================"

# Check if we're in the right directory
if [ ! -f "app.py" ]; then
    echo "❌ Error: app.py not found. Please run this script from the Backend1 directory."
    exit 1
fi

# Check if dependencies are installed
echo "🔍 Checking dependencies..."
python3 -c "import flask, pandas, sklearn, shap" 2>/dev/null
if [ $? -ne 0 ]; then
    echo "📦 Installing Python dependencies..."
    pip3 install --break-system-packages -r requirements.txt
fi

# Check if frontend dependencies are installed
if [ ! -d "frontend-new1/node_modules" ]; then
    echo "📦 Installing frontend dependencies..."
    cd frontend-new1
    npm install --legacy-peer-deps
    cd ..
fi

echo "🚀 Starting PDMS system..."
echo "📊 Backend will run on: http://localhost:5000"
echo "🌐 Frontend will run on: http://localhost:3000"
echo ""
echo "Press Ctrl+C to stop the system"
echo "============================================================"

# Start the system
python3 start_system.py