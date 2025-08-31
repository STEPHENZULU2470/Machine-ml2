# Intrusion Detection System (IDS) - Machine Learning Project

A comprehensive Intrusion Detection System that uses machine learning to detect network threats and anomalies in real-time.

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- Linux/macOS/Windows (with WSL recommended for Windows)
- At least 4GB RAM
- Internet connection for package installation

### Installation & Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd <repository-name>
   ```

2. **Navigate to the backend directory**
   ```bash
   cd Backend1
   ```

3. **Use the automated startup script (Recommended)**
   ```bash
   chmod +x start.sh
   ./start.sh
   ```

4. **Or set up manually**
   ```bash
   # Create virtual environment
   python3 -m venv venv
   source venv/bin/activate  # On Linux/macOS
   # venv\Scripts\activate  # On Windows
   
   # Install dependencies
   pip install -r requirements.txt
   
   # Create necessary directories
   mkdir -p dataset uploads
   
   # Train initial model (if not already present)
   python3 train_model.py
   
   # Start the application
   python3 app.py
   ```

## 🏗️ Project Structure

```
├── Backend1/                    # Main backend application
│   ├── app.py                   # Flask web application
│   ├── requirements.txt         # Python dependencies
│   ├── start.sh                 # Automated startup script
│   ├── TROUBLESHOOTING.md       # Troubleshooting guide
│   ├── test_system.py           # System test script
│   ├── *.py                     # Core Python modules
│   ├── dataset/                 # Dataset storage
│   ├── uploads/                 # File uploads
│   └── venv/                    # Virtual environment
├── auto_datasets/               # Pre-built datasets
│   ├── merged.csv               # Combined dataset
│   └── nsl_kdd.csv             # NSL-KDD dataset
└── .github/                     # GitHub workflows
```

## 🔧 Features

- **Real-time Network Monitoring**: Live packet capture and analysis
- **Machine Learning Detection**: Random Forest classifier with SHAP explanations
- **Web Interface**: Flask-based REST API and dashboard
- **File Upload & Processing**: Support for CSV datasets
- **Model Retraining**: Automatic model updates with new data
- **Threat Alerts**: Real-time notifications and logging
- **Performance Metrics**: Accuracy, precision, recall, and F1-score tracking

## 📊 API Endpoints

- `GET /` - Health check and system status
- `POST /upload` - Upload CSV files for analysis
- `POST /predict` - Get predictions on uploaded data
- `GET /metrics` - Current model performance metrics
- `GET /history` - Recent prediction history
- `GET /forensic-log` - Download forensic analysis logs
- `POST /retrain` - Retrain the model with new data

## 🧪 Testing

Run the comprehensive system test:
```bash
cd Backend1
source venv/bin/activate
python3 test_system.py
```

## 🐛 Troubleshooting

If you encounter issues:

1. **Check the troubleshooting guide**: `Backend1/TROUBLESHOOTING.md`
2. **Run the system test**: `python3 test_system.py`
3. **Verify dependencies**: Ensure all packages are installed
4. **Check file permissions**: Ensure proper access to directories

## 📚 Documentation

- **Backend README**: `Backend1/README.md` - Detailed backend setup
- **Troubleshooting**: `Backend1/TROUBLESHOOTING.md` - Common issues and solutions
- **System Test**: `Backend1/test_system.py` - Comprehensive system validation

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🆘 Support

For support and questions:
1. Check the troubleshooting guide
2. Review the documentation
3. Open an issue on GitHub
4. Check the system test output for diagnostics

## 🔄 Updates

The system automatically:
- Retrains models with new data
- Updates feature sets
- Maintains performance metrics
- Logs all activities for analysis

---

**Status**: ✅ All systems operational and tested
**Last Updated**: January 2025
**Version**: 1.0.0