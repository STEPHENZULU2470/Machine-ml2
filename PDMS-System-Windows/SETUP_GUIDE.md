# 🛡️ PDMS System - Complete Setup Guide

## 📦 What You Have

A complete AI-powered intrusion detection system with:
- **🔧 Backend**: Flask API with ML models
- **🌐 Frontend**: React dashboard with audio alerts
- **🔊 Alert System**: Audio notifications for threats
- **📁 File Upload**: Support for any CSV dataset

## 🚀 Quick Setup (Recommended)

### 1. Navigate to the project
```bash
cd ~/Desktop/PDMS-System
```

### 2. Start the complete system
```bash
./start-system.sh
```

### 3. Open your browser
Go to: **http://localhost:3000**

That's it! The system will automatically:
- Install all dependencies
- Start both backend and frontend
- Open the dashboard interface

## 🔧 Manual Setup (Alternative)

### Backend Setup
```bash
cd backend
pip install -r requirements.txt
python app.py
```

### Frontend Setup (New Terminal)
```bash
cd frontend
npm install
npm run dev
```

## 🎯 How to Use Your System

### 1. **Upload Any Dataset**
- Open http://localhost:3000
- Go to "Upload Dataset" tab
- Drag your CSV file or click to browse
- Choose "Analyze for Threats" for instant analysis
- **Listen for audio alerts** when threats are detected! 🔊

### 2. **Monitor Real-time**
- Check the "Dashboard" for live system status
- Watch threat metrics and statistics
- See active alerts with visual indicators
- Monitor system health and performance

### 3. **Respond to Threats**
- Go to "Threat Actions" tab
- Enter malicious IP addresses
- Choose to Block, Report, or Trace threats
- Test alert sounds with the preview button

### 4. **Manage ML Model**
- Go to "Model Status" tab
- View current model performance metrics
- Upload training data for model improvement
- Retrain the model with new datasets

## 🔊 Alert System Features

### Audio Alerts
- **🟢 Low Threats**: Gentle notification beep
- **🟡 Medium Threats**: Standard alarm tone
- **🟠 High Threats**: Urgent alarm sequence
- **🔴 Critical Threats**: Continuous urgent alarm

### When Alerts Play
- ✅ **Threat Detection**: When malicious traffic is found
- ✅ **Upload Success**: When files are processed successfully
- ✅ **Action Completion**: When threat responses complete
- ✅ **System Events**: For important status changes

### Testing Alerts
Click "Test Alert Sounds" in the Threat Actions tab to preview all sound levels.

## 📁 Dataset Support

### Supported Formats
Upload any CSV file with network traffic data:

- **Network logs** from firewalls or routers
- **Packet capture** data (processed)
- **Security event** logs
- **Custom traffic** data in CSV format

### Example Datasets
- Use the included `demo-dataset.csv` for testing
- Download NSL-KDD dataset for benchmarking
- Use your own network logs converted to CSV

### Required Columns
The system works with any CSV structure. Common columns:
- `duration`, `src_bytes`, `dst_bytes`
- `protocol`, `service`, `flag`
- `src_ip`, `dst_ip` (for threat response)
- `label` or `class` (for training: 'normal' vs 'attack')

## 🌐 System Architecture

```
Frontend (React)     Backend (Flask)      ML Models
     |                     |                  |
Port 3000 ←→ API calls → Port 5000 ←→ → rf_model.joblib
     |                     |                  |
   User UI              REST API          SHAP explainer
     |                     |                  |
Audio Alerts ←→ WebSocket ←→ Threat Detection ←→ Feature Analysis
```

## 🔍 Troubleshooting

### Backend Issues
```bash
# If port 5000 is busy
pkill -f "python.*app.py"

# If modules missing
pip install --break-system-packages -r requirements.txt

# If permission errors
sudo pip install -r requirements.txt
```

### Frontend Issues
```bash
# If port 3000 is busy
pkill -f "npm.*dev"

# If dependencies fail
rm -rf node_modules package-lock.json
npm install --legacy-peer-deps

# If build errors
npm cache clean --force
npm install
```

### Audio Issues
- **No sound**: Check browser audio permissions
- **Alerts not working**: Enable notifications when prompted
- **Audio blocked**: Click anywhere on the page to enable audio

## 📊 System Requirements

### Minimum Requirements
- **OS**: Linux, macOS, or Windows
- **Python**: 3.8+
- **Node.js**: 16+
- **RAM**: 2GB available
- **Storage**: 1GB free space

### Recommended Requirements
- **Python**: 3.13+
- **Node.js**: 22+
- **RAM**: 4GB available
- **Browser**: Chrome 88+ or Firefox 85+

## 🎉 Ready to Protect Your Network!

Your PDMS system includes:

✅ **Complete integration** between backend and frontend
✅ **Audio alert system** for real-time threat notifications
✅ **Universal file upload** for any CSV dataset
✅ **Beautiful dashboard** with live monitoring
✅ **Threat response** capabilities
✅ **Model management** and retraining tools

### Next Steps:
1. Start the system: `./start-system.sh`
2. Open the dashboard: http://localhost:3000
3. Upload your first dataset
4. Listen for audio alerts when threats are detected!

**Your network security system is ready to deploy!** 🛡️🔊