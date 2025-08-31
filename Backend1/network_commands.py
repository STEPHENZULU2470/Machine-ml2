# Network Commands Generator for IDS Testing
import subprocess
import time
import socket
import requests

def run_ping_commands():
    """Run ping commands to generate ICMP traffic"""
    print("🏓 Running ping commands...")
    
    hosts = ["8.8.8.8", "1.1.1.1", "208.67.222.222", "google.com"]
    
    for host in hosts:
        try:
            print(f"Pinging {host}...")
            result = subprocess.run(['ping', '-n', '2', host], 
                                  capture_output=True, text=True, timeout=10)
            if result.returncode == 0:
                print(f"✅ Ping to {host}: Success")
            else:
                print(f"❌ Ping to {host}: Failed")
        except Exception as e:
            print(f"❌ Ping to {host} failed: {e}")
        time.sleep(1)

def run_nslookup_commands():
    """Run nslookup commands to generate DNS traffic"""
    print("\n🔍 Running nslookup commands...")
    
    domains = ["google.com", "github.com", "stackoverflow.com", "microsoft.com"]
    
    for domain in domains:
        try:
            print(f"Looking up {domain}...")
            result = subprocess.run(['nslookup', domain], 
                                  capture_output=True, text=True, timeout=10)
            if result.returncode == 0:
                print(f"✅ nslookup {domain}: Success")
            else:
                print(f"❌ nslookup {domain}: Failed")
        except Exception as e:
            print(f"❌ nslookup {domain} failed: {e}")
        time.sleep(1)

def run_http_requests():
    """Run HTTP requests to generate web traffic"""
    print("\n🌐 Running HTTP requests...")
    
    urls = [
        "http://www.google.com",
        "http://www.github.com",
        "http://www.stackoverflow.com"
    ]
    
    for url in urls:
        try:
            print(f"Requesting {url}...")
            response = requests.get(url, timeout=5)
            print(f"✅ HTTP request to {url}: {response.status_code}")
        except Exception as e:
            print(f"❌ HTTP request to {url} failed: {e}")
        time.sleep(1)

def main():
    """Main function to run all network commands"""
    print("🚀 Network Commands Generator for IDS Testing")
    print("=" * 50)
    print("This script will generate various types of network traffic")
    print("that the IDS system should detect and analyze.")
    print("=" * 50)
    
    # Run different types of network commands
    run_ping_commands()
    run_nslookup_commands()
    run_http_requests()
    
    print("\n✅ All network commands completed!")
    print("Check the backend logs to see the IDS system detecting this traffic.")

if __name__ == "__main__":
    main()
