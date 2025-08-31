#!/usr/bin/env python3
"""
Integration test for the complete PDMS system.
Tests backend API endpoints and simulates frontend interactions.
"""

import requests
import time
import json
import os
import sys
from pathlib import Path

BASE_URL = 'http://localhost:5000'

def test_backend_health():
    """Test if backend is running and responsive"""
    try:
        response = requests.get(f'{BASE_URL}/', timeout=5)
        if response.status_code == 200:
            print("✅ Backend health check passed")
            return True
        else:
            print(f"❌ Backend health check failed: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Backend not reachable: {e}")
        return False

def test_system_status():
    """Test system status endpoint"""
    try:
        response = requests.get(f'{BASE_URL}/system-status', timeout=5)
        if response.status_code == 200:
            data = response.json()
            print(f"✅ System status: {data.get('status', 'unknown')}")
            print(f"   Packets analyzed: {data.get('total_packets_analyzed', 0)}")
            print(f"   Threats detected: {data.get('threats_detected', 0)}")
            return True
        else:
            print(f"❌ System status check failed: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ System status error: {e}")
        return False

def test_metrics():
    """Test metrics endpoint"""
    try:
        response = requests.get(f'{BASE_URL}/metrics', timeout=5)
        if response.status_code == 200:
            data = response.json()
            print("✅ Model metrics retrieved:")
            for metric, value in data.items():
                if value is not None:
                    print(f"   {metric}: {value:.4f}" if isinstance(value, float) else f"   {metric}: {value}")
            return True
        else:
            print(f"❌ Metrics check failed: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Metrics error: {e}")
        return False

def test_file_upload():
    """Test file upload functionality"""
    try:
        # Create a simple test CSV
        test_csv_path = 'test_upload.csv'
        with open(test_csv_path, 'w') as f:
            f.write('duration,src_bytes,dst_bytes,land,wrong_fragment\n')
            f.write('0,100,200,0,0\n')
            f.write('1,500,300,0,0\n')
        
        # Test upload
        with open(test_csv_path, 'rb') as f:
            files = {'file': f}
            response = requests.post(f'{BASE_URL}/predict_uploaded_simple', files=files, timeout=30)
        
        # Clean up
        os.remove(test_csv_path)
        
        if response.status_code == 200:
            data = response.json()
            print("✅ File upload and prediction test passed")
            print(f"   Benign: {data.get('benign_count', 0)}")
            print(f"   Malicious: {data.get('malicious_count', 0)}")
            return True
        else:
            print(f"❌ File upload test failed: {response.status_code}")
            return False
            
    except Exception as e:
        print(f"❌ File upload error: {e}")
        return False

def test_alert_system():
    """Test alert system"""
    try:
        response = requests.post(f'{BASE_URL}/test-alert', 
                                json={'threat_level': 'medium'}, 
                                timeout=5)
        if response.status_code == 200:
            print("✅ Alert system test passed")
            return True
        else:
            print(f"❌ Alert system test failed: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Alert system error: {e}")
        return False

def main():
    """Run all integration tests"""
    print("🧪 PDMS System Integration Test")
    print("=" * 50)
    
    tests = [
        ("Backend Health", test_backend_health),
        ("System Status", test_system_status),
        ("Model Metrics", test_metrics),
        ("File Upload", test_file_upload),
        ("Alert System", test_alert_system),
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        print(f"\n🔍 Testing {test_name}...")
        if test_func():
            passed += 1
        time.sleep(1)
    
    print("\n" + "=" * 50)
    print(f"📊 Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All integration tests passed! System is ready.")
        print("\n📝 Next steps:")
        print("1. Start the system: ./start.sh")
        print("2. Open frontend: http://localhost:3000")
        print("3. Upload CSV files for threat analysis")
        print("4. Monitor alerts and system status")
        return 0
    else:
        print("❌ Some tests failed. Please check the errors above.")
        return 1

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == '--help':
        print("PDMS Integration Test")
        print("Usage: python3 test_system_integration.py")
        print("\nThis script tests the backend API endpoints to ensure")
        print("the system is working correctly before starting the frontend.")
        sys.exit(0)
    
    sys.exit(main())