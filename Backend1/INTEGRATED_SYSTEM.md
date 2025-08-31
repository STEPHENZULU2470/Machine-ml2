# 🛡️ PDMS - Complete Integrated System

## 🚀 Quick Start

### Option 1: One-Command Start
```bash
cd Backend1
./start.sh
```

### Option 2: Manual Start
```bash
# Terminal 1 - Backend
cd Backend1
python3 app.py

# Terminal 2 - Frontend  
cd Backend1/frontend-new1
npm run dev
```

## 🌐 Access Points

- **Frontend UI**: http://localhost:3000
- **Backend API**: http://localhost:5000
- **API Documentation**: http://localhost:5000 (health check)

## 🎯 Features

### 📁 **Dataset Upload & Analysis**
- **Drag & Drop**: Drop any CSV file onto the upload area
- **Instant Analysis**: Get immediate threat detection results
- **Real-time Alerts**: Audio alerts for detected threats
- **Multiple Formats**: Supports any CSV dataset structure

### 🔊 **Alert System**
- **Audio Alerts**: Different sounds for different threat levels
  - 🟢 **Low**: Gentle beep
  - 🟡 **Medium**: Standard alarm
  - 🟠 **High**: Urgent alarm
  - 🔴 **Critical**: Continuous urgent alarm
- **Visual Notifications**: Browser notifications for threats
- **Real-time Updates**: Live threat monitoring

### 📊 **Dashboard Features**
- **System Status**: Real-time system health monitoring
- **Threat Metrics**: Live statistics and performance indicators
- **Live Traffic**: Real-time packet analysis (when TShark available)
- **Model Performance**: Accuracy, precision, recall, F1-score

### 🛠️ **Threat Response Actions**
- **Block IP**: Instantly block malicious IP addresses
- **Report Threats**: Report threats to security systems
- **Trace Connections**: Trace network connections for forensics
- **Test Alerts**: Test alert system with different threat levels

### 🧠 **Model Management**
- **Retrain Model**: Upload new datasets to retrain the AI model
- **Performance Metrics**: Monitor model accuracy and performance
- **Model Comparison**: Compare different ML algorithms
- **Feature Analysis**: SHAP explanations for predictions

## 🔧 How to Use

### 1. **Upload a Dataset**
1. Go to the "Upload Dataset" tab
2. Drag and drop your CSV file or click to browse
3. Choose "Analyze for Threats" for immediate analysis
4. Choose "Upload for Retraining" to improve the model

### 2. **Monitor Threats**
1. Check the "Dashboard" for real-time status
2. Watch for audio alerts when threats are detected
3. View live predictions in the traffic analysis section

### 3. **Respond to Threats**
1. Go to "Threat Actions" tab
2. Enter the malicious IP address
3. Choose to Block, Report, or Trace the threat
4. Test alert sounds with the "Test Alert Sounds" button

### 4. **Manage the Model**
1. Go to "Model Status" tab
2. View current model performance metrics
3. Click "Retrain Model" after uploading new training data
4. Monitor model comparison results

## 📋 **Supported Dataset Formats**

The system accepts any CSV file with network traffic data. Common formats include:

- **NSL-KDD Dataset**: Standard intrusion detection dataset
- **CICIDS Dataset**: Canadian Institute for Cybersecurity dataset  
- **Custom Network Logs**: Any CSV with network features
- **Firewall Logs**: Converted to CSV format
- **Packet Captures**: Processed network packet data

### Required/Recommended Columns:
- `duration`, `src_bytes`, `dst_bytes`
- `protocol`, `service`, `flag`
- `src_ip`, `dst_ip` (for threat response)
- `label` (for retraining - 'normal' or 'attack')

## 🔊 **Alert Sound System**

The system provides rich audio feedback:

- **🎵 Upload Success**: Ascending musical notes
- **⚠️ Threat Detected**: Alarm based on severity level
- **❌ Error**: Descending warning tones
- **🔔 System Events**: Various notification sounds

## 🚨 **Real-time Monitoring**

When TShark is available, the system provides:
- Live packet capture and analysis
- Real-time threat detection
- Automatic alert generation
- Forensic logging

## 🛠️ **Troubleshooting**

### Common Issues:

1. **"Connection Error"**: Backend not running
   - Solution: Start backend with `python3 app.py`

2. **"TShark not found"**: Network capture disabled
   - Solution: Install Wireshark/TShark (optional for file analysis)

3. **"Module not found"**: Missing dependencies
   - Solution: Run `pip3 install --break-system-packages -r requirements.txt`

4. **Frontend won't start**: Missing Node.js dependencies
   - Solution: Run `npm install --legacy-peer-deps` in frontend-new1/

### 🔧 **Manual Setup**

If the automatic startup doesn't work:

```bash
# 1. Install Python dependencies
cd Backend1
pip3 install --break-system-packages -r requirements.txt

# 2. Install frontend dependencies  
cd frontend-new1
npm install --legacy-peer-deps

# 3. Start backend (Terminal 1)
cd ../
python3 app.py

# 4. Start frontend (Terminal 2)
cd frontend-new1
npm run dev
```

## 🎉 **You're Ready!**

Your PDMS system is now fully integrated with:
- ✅ File upload and analysis
- ✅ Real-time threat detection
- ✅ Audio alert system
- ✅ Visual dashboard
- ✅ Threat response actions
- ✅ Model management

Open http://localhost:3000 and start analyzing your datasets!