# 🛡️ PDMS - AI-Powered Intrusion Detection & Mitigation System

A complete, integrated cybersecurity solution with machine learning-based threat detection, real-time monitoring, and automated response capabilities.

## 🚀 Quick Start

### One-Command Setup
```bash
cd backend
./start.sh
```

Then open your browser to: **http://localhost:3000**

## 📁 Project Structure

```
PDMS-System/
├── backend/              # Flask API server
│   ├── app.py           # Main Flask application
│   ├── requirements.txt # Python dependencies
│   ├── start.sh         # Easy startup script
│   ├── models/          # ML model files
│   └── ...
├── frontend/            # React web interface
│   ├── src/             # React source code
│   ├── package.json     # Node.js dependencies
│   └── ...
└── README.md           # This file
```

## 🎯 Key Features

### 🔊 **Audio Alert System**
- **Real-time audio alerts** for threat detection
- **4 threat levels** with unique sounds (Low, Medium, High, Critical)
- **Success/error sounds** for user actions
- **Test functionality** to preview all alerts

### 📁 **Universal Dataset Upload**
- **Drag & drop interface** for any CSV file
- **Instant threat analysis** with detailed results
- **Model retraining** with new datasets
- **Support for multiple dataset formats**

### 📊 **Real-time Dashboard**
- **Live system monitoring** with health metrics
- **Threat statistics** and performance indicators
- **Active alert management** with visual indicators
- **Model performance** tracking

### 🛡️ **Threat Response**
- **IP blocking** for malicious addresses
- **Threat reporting** to security systems
- **Network tracing** for forensic analysis
- **Manual threat management** tools

## 🔧 Setup Instructions

### Prerequisites
- Python 3.8+ (Python 3.13+ recommended)
- Node.js 16+ (Node.js 22+ recommended)
- npm or yarn package manager

### Backend Setup
```bash
cd backend
pip install -r requirements.txt
python app.py
```

### Frontend Setup
```bash
cd frontend
npm install
npm run dev
```

### Integrated Setup
```bash
cd backend
./start.sh  # Starts both backend and frontend
```

## 🌐 Access Points

- **Frontend Dashboard**: http://localhost:3000
- **Backend API**: http://localhost:5000
- **API Health Check**: http://localhost:5000/

## 📋 Supported Datasets

The system accepts any CSV file with network traffic data:

- **NSL-KDD Dataset** (standard benchmark)
- **CICIDS Dataset** (modern intrusion detection)
- **Custom Network Logs** (any CSV format)
- **Firewall Logs** (converted to CSV)
- **Packet Capture Data** (processed network packets)

### Common Column Names:
- Network features: `duration`, `src_bytes`, `dst_bytes`, `protocol`
- IP addresses: `src_ip`, `dst_ip` (for threat response)
- Labels: `label`, `class` (for model training)

## 🔊 Alert System Usage

### Automatic Alerts
- **Threat Detection**: Plays when malicious traffic is found
- **System Events**: Audio feedback for uploads and actions
- **Real-time Monitoring**: Continuous background monitoring

### Manual Testing
1. Go to "Threat Actions" tab
2. Click "Test Alert Sounds"
3. Listen to all 4 threat levels

### Browser Notifications
- Enable notifications when prompted
- Get desktop alerts for critical threats
- Visual and audio notifications combined

## 🛠️ How to Use

### 1. **Upload & Analyze Datasets**
1. Open http://localhost:3000
2. Go to "Upload Dataset" tab
3. Drag your CSV file or click to browse
4. Click "Analyze for Threats"
5. Listen for audio alerts if threats are found!

### 2. **Monitor Real-time Status**
1. Check the "Dashboard" tab
2. Monitor system health and metrics
3. Watch for live threat alerts
4. View active threat indicators

### 3. **Respond to Threats**
1. Go to "Threat Actions" tab
2. Enter malicious IP address
3. Choose action: Block, Report, or Trace
4. Get audio confirmation of actions

### 4. **Manage ML Model**
1. Go to "Model Status" tab
2. View current model performance
3. Upload new training data
4. Click "Retrain Model" to improve accuracy

## 🔧 Troubleshooting

### Backend Issues
- **Port 5000 in use**: Kill existing Flask processes
- **Module errors**: Run `pip install -r requirements.txt`
- **Permission errors**: Use `--break-system-packages` flag

### Frontend Issues  
- **Port 3000 in use**: Kill existing Node processes
- **Dependency conflicts**: Use `npm install --legacy-peer-deps`
- **Build errors**: Delete `node_modules` and reinstall

### Network Capture Issues
- **TShark not found**: Install Wireshark (optional for file analysis)
- **Permission denied**: Run with appropriate network permissions
- **No interfaces**: Normal in containerized environments

## 📊 API Endpoints

### Core Endpoints
- `GET /` - Health check
- `GET /system-status` - System status and metrics
- `POST /upload` - Upload CSV for retraining
- `POST /predict_uploaded_simple` - Upload and analyze CSV

### Monitoring
- `GET /metrics` - Model performance metrics
- `GET /live-predictions` - Live threat predictions
- `GET /alerts` - Active threat alerts
- `GET /threat-analysis` - Threat analysis data

### Actions
- `POST /block` - Block IP address
- `POST /report` - Report threat
- `POST /trace` - Trace connection
- `POST /test-alert` - Test alert system

## 🎉 You're Ready!

Your PDMS system is now fully set up with:
- ✅ Integrated backend and frontend
- ✅ Audio alert system for threats
- ✅ File upload for any dataset type
- ✅ Real-time monitoring dashboard
- ✅ Threat response capabilities
- ✅ Model management tools

**Start the system and begin protecting your network!** 🛡️