# 🔧 PDMS Backend - Flask API Server

This is the backend API server for the PDMS (AI-Powered Intrusion Detection & Mitigation System).

## 🚀 Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Start the server
python app.py
```

Server runs on: **http://localhost:5000**

## 📋 Dependencies

All Python dependencies are listed in `requirements.txt` with pinned versions:

- **Flask 3.1.2** - Web framework
- **Flask-CORS 6.0.1** - Cross-origin resource sharing
- **Pandas 2.3.2** - Data manipulation
- **Scikit-learn 1.7.1** - Machine learning
- **SHAP 0.48.0** - Model explanations
- **PyShark 0.6** - Network packet analysis
- **Requests 2.32.5** - HTTP client

## 🌐 API Endpoints

### Core Functionality
- `GET /` - Health check
- `GET /system-status` - Complete system status
- `POST /upload` - Upload CSV for retraining
- `POST /predict_uploaded_simple` - Upload and analyze CSV

### Real-time Monitoring
- `GET /live-predictions` - Live threat predictions
- `GET /alerts` - Active threat alerts
- `GET /metrics` - Model performance metrics
- `GET /threat-analysis` - Threat analysis data

### Threat Response
- `POST /block` - Block IP address
- `POST /report` - Report threat to security systems
- `POST /trace` - Trace network connection
- `POST /test-alert` - Test alert system

## 🤖 Machine Learning

### Model Files
- `rf_model.joblib` - Random Forest classifier
- `shap_explainer.joblib` - SHAP explainer for interpretability
- `features.txt` - List of 115 network features

### Training Data
- Place training CSV in `uploads/` directory
- Use `/retrain` endpoint to retrain model
- Supports any labeled network traffic dataset

## 🔊 Alert System

The backend triggers alerts through:
- WebSocket connections (future enhancement)
- HTTP polling from frontend
- Direct API calls to `/test-alert`

## 📊 Data Processing

### Supported CSV Formats
- **NSL-KDD** - Standard intrusion detection dataset
- **CICIDS** - Canadian Institute cybersecurity data
- **Custom formats** - Any network traffic CSV

### Required Features
The model expects 115 specific network features. Missing features are automatically filled with zeros.

## 🛠️ Configuration

### Environment Variables
- `FLASK_ENV=development` - Development mode
- `FLASK_DEBUG=1` - Enable debug mode

### File Paths
- `uploads/` - Uploaded CSV files
- `forensic_log.csv` - Security event log
- Model files in root directory

## 🔍 Logging

- **Console output** - Real-time status updates
- **Forensic log** - All security events
- **Error logging** - Exception tracking

## 🚨 Security Features

- **Real-time packet analysis** (when TShark available)
- **Automated threat detection** using ML
- **Threat response actions** (block, report, trace)
- **Forensic logging** for investigation

## 🐛 Troubleshooting

### Common Issues

1. **TShark not found**
   - Live packet capture disabled
   - File-based analysis still works
   - Install Wireshark for full functionality

2. **Model version warnings**
   - Models trained with sklearn 1.7.0
   - Running on sklearn 1.7.1
   - Functionality not affected

3. **Permission errors**
   - Use `--break-system-packages` for pip
   - Run with appropriate network permissions for packet capture

## 📈 Performance

- **Real-time analysis** of uploaded datasets
- **Sub-second predictions** for individual packets
- **Scalable architecture** for high-traffic environments
- **Efficient memory usage** with streaming processing