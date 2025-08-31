# Simple Network Test Script
import subprocess
import time
import requests

def run_network_tests():
    print("🚀 Running Network Tests for IDS Detection")
    print("=" * 50)
    
    # Test 1: Ping
    print("1. Running ping test...")
    try:
        result = subprocess.run(['ping', '-n', '3', '8.8.8.8'], 
                              capture_output=True, text=True, timeout=10)
        print("✅ Ping completed")
    except Exception as e:
        print(f"❌ Ping failed: {e}")
    
    time.sleep(2)
    
    # Test 2: DNS Lookup
    print("\n2. Running DNS lookup...")
    try:
        result = subprocess.run(['nslookup', 'google.com'], 
                              capture_output=True, text=True, timeout=10)
        print("✅ DNS lookup completed")
    except Exception as e:
        print(f"❌ DNS lookup failed: {e}")
    
    time.sleep(2)
    
    # Test 3: HTTP Request
    print("\n3. Running HTTP request...")
    try:
        response = requests.get('http://www.google.com', timeout=5)
        print(f"✅ HTTP request completed: {response.status_code}")
    except Exception as e:
        print(f"❌ HTTP request failed: {e}")
    
    print("\n" + "=" * 50)
    print("✅ Network tests completed!")
    print("Check the backend logs for packet detection.")

def check_ids_status():
    print("\n🔍 Checking IDS System Status...")
    try:
        response = requests.get('http://localhost:5000/system-status', timeout=5)
        if response.status_code == 200:
            data = response.json()
            print(f"📦 Total Packets Analyzed: {data['total_packets_analyzed']}")
            print(f"🚨 Threats Detected: {data['threats_detected']}")
            print(f"📊 Threat Rate: {data['threat_rate']}%")
        else:
            print("❌ Could not get system status")
    except Exception as e:
        print(f"❌ Error checking status: {e}")

if __name__ == "__main__":
    run_network_tests()
    check_ids_status()