# -*- coding: utf-8 -*-
import os
import time
import requests

def generate_ping():
    print("Pinging google.com ...")
    os.system("ping -n 4 google.com" if os.name == 'nt' else "ping -c 4 google.com")

def generate_http():
    print("Making HTTP requests to http://example.com ...")
    for _ in range(3):
        try:
            r = requests.get("http://example.com", timeout=3)
            print(f"Status: {r.status_code}")
        except Exception as e:
            print(f"HTTP request failed: {e}")
        time.sleep(1)

def main():
    generate_ping()
    generate_http()
    print("Test traffic generation complete.")

if __name__ == "__main__":
    main()
