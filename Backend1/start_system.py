#!/usr/bin/env python3
"""
Startup script for the complete PDMS system.
Starts both backend Flask server and frontend React dev server.
"""

import subprocess
import sys
import os
import time
import signal
import threading
from pathlib import Path

class PDMSSystem:
    def __init__(self):
        self.backend_process = None
        self.frontend_process = None
        self.running = True
        
    def start_backend(self):
        """Start the Flask backend server"""
        print("🚀 Starting Flask backend server...")
        try:
            self.backend_process = subprocess.Popen(
                [sys.executable, 'app.py'],
                cwd=Path(__file__).parent,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                universal_newlines=True,
                bufsize=1
            )
            
            # Monitor backend output
            def monitor_backend():
                for line in iter(self.backend_process.stdout.readline, ''):
                    if self.running:
                        print(f"[BACKEND] {line.strip()}")
                    else:
                        break
            
            threading.Thread(target=monitor_backend, daemon=True).start()
            print("✅ Backend server started on http://localhost:5000")
            
        except Exception as e:
            print(f"❌ Failed to start backend: {e}")
            return False
        
        return True
    
    def start_frontend(self):
        """Start the React frontend dev server"""
        print("🌐 Starting React frontend server...")
        try:
            frontend_dir = Path(__file__).parent / 'frontend-new1'
            
            self.frontend_process = subprocess.Popen(
                ['npm', 'run', 'dev'],
                cwd=frontend_dir,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                universal_newlines=True,
                bufsize=1
            )
            
            # Monitor frontend output
            def monitor_frontend():
                for line in iter(self.frontend_process.stdout.readline, ''):
                    if self.running:
                        print(f"[FRONTEND] {line.strip()}")
                    else:
                        break
            
            threading.Thread(target=monitor_frontend, daemon=True).start()
            print("✅ Frontend server starting on http://localhost:3000")
            
        except Exception as e:
            print(f"❌ Failed to start frontend: {e}")
            return False
        
        return True
    
    def stop_system(self):
        """Stop both backend and frontend servers"""
        print("\n🛑 Stopping PDMS system...")
        self.running = False
        
        if self.backend_process:
            self.backend_process.terminate()
            try:
                self.backend_process.wait(timeout=5)
                print("✅ Backend stopped")
            except subprocess.TimeoutExpired:
                self.backend_process.kill()
                print("⚠️ Backend force killed")
        
        if self.frontend_process:
            self.frontend_process.terminate()
            try:
                self.frontend_process.wait(timeout=5)
                print("✅ Frontend stopped")
            except subprocess.TimeoutExpired:
                self.frontend_process.kill()
                print("⚠️ Frontend force killed")
    
    def run(self):
        """Run the complete system"""
        print("🔧 PDMS - AI-Powered Intrusion Detection & Mitigation System")
        print("=" * 60)
        
        # Setup signal handlers for graceful shutdown
        signal.signal(signal.SIGINT, lambda s, f: self.stop_system())
        signal.signal(signal.SIGTERM, lambda s, f: self.stop_system())
        
        try:
            # Start backend first
            if not self.start_backend():
                return 1
            
            # Wait a moment for backend to initialize
            time.sleep(3)
            
            # Start frontend
            if not self.start_frontend():
                self.stop_system()
                return 1
            
            print("\n🎉 PDMS System is now running!")
            print("📊 Backend API: http://localhost:5000")
            print("🌐 Frontend UI: http://localhost:3000")
            print("\nPress Ctrl+C to stop the system")
            print("=" * 60)
            
            # Keep the main process alive
            try:
                while self.running:
                    time.sleep(1)
                    
                    # Check if processes are still running
                    if self.backend_process and self.backend_process.poll() is not None:
                        print("❌ Backend process died")
                        break
                    
                    if self.frontend_process and self.frontend_process.poll() is not None:
                        print("❌ Frontend process died")
                        break
                        
            except KeyboardInterrupt:
                pass
            
        except Exception as e:
            print(f"❌ System error: {e}")
            return 1
        finally:
            self.stop_system()
        
        return 0

def main():
    """Main entry point"""
    system = PDMSSystem()
    return system.run()

if __name__ == '__main__':
    sys.exit(main())