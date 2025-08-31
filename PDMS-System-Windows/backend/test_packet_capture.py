#!/usr/bin/env python3
"""
Test script to check if packet capture is working
"""

import pyshark
import time
import sys

def test_packet_capture():
    """Test if we can capture packets"""
    print("🔍 Testing packet capture...")
    
    try:
        # Try to create a capture object
        print("Creating capture object...")
        capture = pyshark.LiveCapture()
        print("✅ Capture object created successfully")
        
        # Try to capture a few packets
        print("Starting packet capture (will capture 5 packets)...")
        packet_count = 0
        
        for packet in capture.sniff_continuously():
            packet_count += 1
            print(f"📦 Captured packet #{packet_count}")
            
            # Try to extract basic info
            try:
                if hasattr(packet, 'ip'):
                    src = packet.ip.src
                    dst = packet.ip.dst
                    print(f"   Source: {src} -> Destination: {dst}")
                else:
                    print("   No IP layer found")
                    
                if hasattr(packet, 'transport_layer'):
                    proto = packet.transport_layer
                    print(f"   Protocol: {proto}")
                else:
                    print("   No transport layer found")
                    
                print(f"   Length: {packet.length}")
                
            except Exception as e:
                print(f"   Error extracting packet info: {e}")
            
            # Stop after 5 packets
            if packet_count >= 5:
                break
                
        print("✅ Packet capture test completed successfully!")
        return True
        
    except Exception as e:
        print(f"❌ Packet capture test failed: {e}")
        print("This might be due to:")
        print("1. No network traffic")
        print("2. Insufficient permissions (try running as administrator)")
        print("3. No network interfaces available")
        print("4. Wireshark/tshark not installed")
        return False

def test_network_activity():
    """Generate some network activity"""
    print("\n🌐 Generating network activity...")
    
    try:
        import requests
        print("Making HTTP requests to generate traffic...")
        
        urls = ["http://www.google.com", "http://www.github.com"]
        for url in urls:
            try:
                response = requests.get(url, timeout=5)
                print(f"✅ HTTP request to {url}: {response.status_code}")
            except Exception as e:
                print(f"❌ HTTP request to {url} failed: {e}")
            time.sleep(1)
            
    except ImportError:
        print("❌ requests library not available")
    except Exception as e:
        print(f"❌ Network activity test failed: {e}")

if __name__ == "__main__":
    print("🚀 Packet Capture Test")
    print("=" * 40)
    
    # Test network activity first
    test_network_activity()
    
    # Test packet capture
    success = test_packet_capture()
    
    if success:
        print("\n🎉 Packet capture is working!")
        print("The IDS system should be able to detect network traffic.")
    else:
        print("\n⚠️ Packet capture is not working.")
        print("The IDS system may not detect network traffic.")
        print("Try running as administrator or check network interface settings.") 