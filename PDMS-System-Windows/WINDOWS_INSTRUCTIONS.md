# 🪟 Windows Setup Instructions

## 📁 **Copy This Folder to Windows**

1. **Copy** the entire `PDMS-System-Windows` folder
2. **Paste** it to your Windows machine at:
   - **C:\PDMS-System\** (recommended)
   - **D:\PDMS-System\**

## 💻 **Two Terminal Commands for Windows**

### 🔧 **Terminal 1 - Backend (Command Prompt or PowerShell)**

```cmd
cd C:\PDMS-System\backend
pip install -r requirements.txt
python app.py
```

### 🌐 **Terminal 2 - Frontend (Command Prompt or PowerShell)**

```cmd
cd C:\PDMS-System\frontend
npm install --legacy-peer-deps
npm run dev
```

## 🎯 **Access Your System**

After running both terminals, open your browser to:
**http://localhost:3000**

## 🔊 **What You'll Get**

✅ **File upload** with drag & drop for any CSV
✅ **Audio alerts** when threats are detected
✅ **Real-time dashboard** with live monitoring
✅ **Threat response** actions (block, report, trace)
✅ **Model management** and retraining

## 📋 **Prerequisites for Windows**

Install these first:
- **Python 3.8+**: https://python.org/downloads/
- **Node.js 16+**: https://nodejs.org/download/

## 🎉 **Ready to Use!**

Your complete AI-powered intrusion detection system with backend and frontend integration, audio alerts, and file upload capabilities!