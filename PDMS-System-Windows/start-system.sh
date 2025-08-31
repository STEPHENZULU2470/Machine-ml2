#!/bin/bash

# PDMS System Startup Script
# Starts both backend Flask server and frontend React dev server

echo "🛡️  PDMS - AI-Powered Intrusion Detection & Mitigation System"
echo "================================================================"
echo ""

# Check if we're in the right directory
if [ ! -d "backend" ] || [ ! -d "frontend" ]; then
    echo "❌ Error: backend or frontend directory not found."
    echo "   Please run this script from the PDMS-System directory."
    exit 1
fi

# Function to check if a port is in use
check_port() {
    local port=$1
    if lsof -Pi :$port -sTCP:LISTEN -t >/dev/null 2>&1; then
        return 0  # Port is in use
    else
        return 1  # Port is free
    fi
}

# Check if ports are available
if check_port 5000; then
    echo "⚠️  Port 5000 is already in use. Please stop the existing Flask server."
    echo "   You can kill it with: pkill -f 'python.*app.py'"
    exit 1
fi

if check_port 3000; then
    echo "⚠️  Port 3000 is already in use. Please stop the existing React server."
    echo "   You can kill it with: pkill -f 'npm.*dev'"
    exit 1
fi

echo "🔍 Checking dependencies..."

# Check Python dependencies
cd backend
echo "📦 Checking Python dependencies..."
python3 -c "import flask, pandas, sklearn, shap, requests" 2>/dev/null
if [ $? -ne 0 ]; then
    echo "📦 Installing Python dependencies..."
    pip3 install --break-system-packages -r requirements.txt
    if [ $? -ne 0 ]; then
        echo "❌ Failed to install Python dependencies. Please install manually."
        exit 1
    fi
fi

# Check Node.js dependencies
cd ../frontend
echo "📦 Checking Node.js dependencies..."
if [ ! -d "node_modules" ]; then
    echo "📦 Installing Node.js dependencies..."
    npm install --legacy-peer-deps
    if [ $? -ne 0 ]; then
        echo "❌ Failed to install Node.js dependencies. Please install manually."
        exit 1
    fi
fi

echo ""
echo "🚀 Starting PDMS system..."
echo "📊 Backend will run on: http://localhost:5000"
echo "🌐 Frontend will run on: http://localhost:3000"
echo ""
echo "⏳ Please wait for both servers to start..."
echo "🔴 Press Ctrl+C to stop the entire system"
echo "================================================================"

# Function to cleanup on exit
cleanup() {
    echo ""
    echo "🛑 Stopping PDMS system..."
    
    # Kill backend
    pkill -f "python.*app.py" 2>/dev/null
    
    # Kill frontend
    pkill -f "npm.*dev" 2>/dev/null
    
    echo "✅ System stopped. Goodbye!"
    exit 0
}

# Set up signal handlers
trap cleanup SIGINT SIGTERM

# Start backend in background
cd ../backend
echo "🔧 Starting Flask backend server..."
python3 app.py > backend.log 2>&1 &
BACKEND_PID=$!

# Wait for backend to start
sleep 5

# Check if backend is running
if ! curl -s http://localhost:5000/ > /dev/null 2>&1; then
    echo "❌ Backend failed to start. Check backend.log for errors."
    kill $BACKEND_PID 2>/dev/null
    exit 1
fi

echo "✅ Backend started successfully"

# Start frontend
cd ../frontend
echo "🌐 Starting React frontend server..."
npm run dev > frontend.log 2>&1 &
FRONTEND_PID=$!

# Wait for frontend to start
sleep 8

echo ""
echo "🎉 PDMS System is now running!"
echo ""
echo "📊 Backend API: http://localhost:5000"
echo "🌐 Frontend UI:  http://localhost:3000"
echo ""
echo "📝 Features available:"
echo "   • Upload any CSV dataset for threat analysis"
echo "   • Real-time audio alerts for detected threats"
echo "   • Interactive dashboard with live metrics"
echo "   • Threat response actions (block, report, trace)"
echo "   • Model retraining with new datasets"
echo ""
echo "🔴 Press Ctrl+C to stop the system"
echo "================================================================"

# Keep script running and monitor processes
while true; do
    # Check if backend is still running
    if ! kill -0 $BACKEND_PID 2>/dev/null; then
        echo "❌ Backend process died. Stopping system..."
        cleanup
    fi
    
    # Check if frontend is still running  
    if ! kill -0 $FRONTEND_PID 2>/dev/null; then
        echo "❌ Frontend process died. Stopping system..."
        cleanup
    fi
    
    sleep 2
done