#!/usr/bin/env python3
"""
Demo script for the IDS System
Shows the main features and capabilities
"""

import os
import time
import json
import requests
from datetime import datetime

def print_header(title):
    """Print a formatted header"""
    print("\n" + "=" * 60)
    print(f"🚀 {title}")
    print("=" * 60)

def print_section(title):
    """Print a formatted section"""
    print(f"\n📋 {title}")
    print("-" * 40)

def check_backend_status():
    """Check if the backend is running"""
    print_section("Checking Backend Status")
    
    try:
        response = requests.get("http://localhost:5000/", timeout=5)
        if response.status_code == 200:
            data = response.json()
            print("✅ Backend is running!")
            print(f"   Status: {data.get('status', 'Unknown')}")
            print(f"   Uptime: {data.get('uptime', 'Unknown')}")
            return True
        else:
            print(f"❌ Backend responded with status {response.status_code}")
            return False
    except requests.exceptions.ConnectionError:
        print("❌ Backend is not running")
        print("   Start it with: python3 app.py")
        return False
    except Exception as e:
        print(f"❌ Error checking backend: {e}")
        return False

def show_system_info():
    """Display system information"""
    print_section("System Information")
    
    # Check model files
    model_files = ['rf_model.joblib', 'shap_explainer.joblib', 'features.txt']
    for file in model_files:
        if os.path.exists(file):
            size = os.path.getsize(file)
            print(f"✅ {file} ({size:,} bytes)")
        else:
            print(f"❌ {file} (missing)")
    
    # Check directories
    dirs = ['dataset', 'uploads', 'venv']
    for dir_name in dirs:
        if os.path.exists(dir_name):
            print(f"✅ {dir_name}/")
        else:
            print(f"❌ {dir_name}/ (missing)")

def show_api_endpoints():
    """Display available API endpoints"""
    print_section("Available API Endpoints")
    
    endpoints = [
        ("GET", "/", "Health check and system status"),
        ("POST", "/upload", "Upload CSV files for analysis"),
        ("POST", "/predict", "Get predictions on uploaded data"),
        ("GET", "/metrics", "Current model performance metrics"),
        ("GET", "/history", "Recent prediction history"),
        ("GET", "/forensic-log", "Download forensic analysis logs"),
        ("POST", "/retrain", "Retrain the model with new data")
    ]
    
    for method, path, description in endpoints:
        print(f"{method:6} {path:<20} - {description}")

def show_usage_examples():
    """Show usage examples"""
    print_section("Usage Examples")
    
    examples = [
        ("Start the system", "python3 app.py"),
        ("Run system tests", "python3 test_system.py"),
        ("Train the model", "python3 train_model.py"),
        ("Generate test traffic", "python3 test_traffic.py"),
        ("Use startup script", "./start.sh")
    ]
    
    for description, command in examples:
        print(f"💡 {description}:")
        print(f"   {command}")

def show_troubleshooting_tips():
    """Show troubleshooting tips"""
    print_section("Troubleshooting Tips")
    
    tips = [
        "If modules are missing: pip install -r requirements.txt",
        "If backend won't start: Check if port 5000 is available",
        "If model files are missing: Run python3 train_model.py",
        "If packet capture fails: Install tshark (sudo apt install tshark)",
        "For more help: See TROUBLESHOOTING.md"
    ]
    
    for tip in tips:
        print(f"🔧 {tip}")

def main():
    """Main demo function"""
    print_header("IDS System Demo")
    
    print("Welcome to the Intrusion Detection System!")
    print("This demo will show you the main features and capabilities.")
    
    # Check backend status
    backend_running = check_backend_status()
    
    # Show system information
    show_system_info()
    
    # Show API endpoints
    show_api_endpoints()
    
    # Show usage examples
    show_usage_examples()
    
    # Show troubleshooting tips
    show_troubleshooting_tips()
    
    # Final status
    print_header("Demo Complete")
    
    if backend_running:
        print("🎉 Your IDS system is ready to use!")
        print("\n🌐 Access the web interface at: http://localhost:5000")
        print("📊 Check system status at: http://localhost:5000/")
        print("📁 Upload files at: http://localhost:5000/upload")
    else:
        print("⚠️  Backend is not running")
        print("\nTo start the system:")
        print("1. cd Backend1")
        print("2. source venv/bin/activate")
        print("3. python3 app.py")
        print("\nOr use the startup script:")
        print("   ./start.sh")
    
    print("\n📚 For more information, see:")
    print("   - README.md (main documentation)")
    print("   - TROUBLESHOOTING.md (common issues)")
    print("   - test_system.py (system validation)")

if __name__ == "__main__":
    main()