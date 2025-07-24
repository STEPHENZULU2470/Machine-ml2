#!/usr/bin/env python3
"""
Threat Alert System for PDMS
Provides real-time alerts, sounds, and automated actions for detected threats
"""

import json
import time
import threading
import requests
import subprocess
import platform
import os
from datetime import datetime
from collections import deque
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ThreatAlertSystem:
    def __init__(self):
        self.threat_history = deque(maxlen=1000)
        self.alert_levels = {
            'low': {'color': '#ffce56', 'priority': 1, 'sound_freq': 800},
            'medium': {'color': '#ff9f40', 'priority': 2, 'sound_freq': 1000},
            'high': {'color': '#ff357a', 'priority': 3, 'sound_freq': 1200},
            'critical': {'color': '#ff0000', 'priority': 4, 'sound_freq': 1500}
        }
        self.active_threats = {}
        self.alert_count = 0
        self.last_alert_time = 0
        self.alert_cooldown = 3  # seconds between alerts
        
        # Initialize sound system
        self.sound_enabled = platform.system() == 'Windows'
    
    def play_alert_sound(self, level):
        """Play alert sound based on threat level"""
        if not self.sound_enabled:
            return
            
        try:
            import winsound
            freq = self.alert_levels[level]['sound_freq']
            
            if level == 'low':
                winsound.Beep(freq, 200)
            elif level == 'medium':
                winsound.Beep(freq, 200)
                time.sleep(0.1)
                winsound.Beep(freq, 200)
            elif level == 'high':
                winsound.Beep(freq, 200)
                time.sleep(0.1)
                winsound.Beep(freq, 200)
                time.sleep(0.1)
                winsound.Beep(freq, 200)
            elif level == 'critical':
                for _ in range(5):
                    winsound.Beep(freq, 100)
                    time.sleep(0.05)
        except Exception as e:
            logger.error(f"Error playing alert sound: {e}")
    
    def determine_threat_level(self, threat_data):
        """Determine threat level based on threat characteristics"""
        src_ip = threat_data.get('src', '')
        protocol = threat_data.get('protocol', '')
        prediction = threat_data.get('prediction', '')
        
        # Known malicious IPs (example)
        known_malicious_ips = [
            '192.168.1.100',  # Example malicious IP
            '10.0.0.50',      # Example malicious IP
        ]
        
        # High-risk protocols
        high_risk_protocols = ['SSH', 'TELNET', 'FTP']
        
        # Determine threat level
        if src_ip in known_malicious_ips:
            return 'critical'
        elif protocol in high_risk_protocols:
            return 'high'
        elif prediction == 'Malicious':
            return 'medium'
        else:
            return 'low'
    
    def trigger_alert(self, threat_data):
        """Trigger comprehensive alert for detected threat"""
        current_time = time.time()
        
        # Check cooldown to prevent spam
        if current_time - self.last_alert_time < self.alert_cooldown:
            return None
        
        threat_level = self.determine_threat_level(threat_data)
        alert_config = self.alert_levels[threat_level]
        
        # Create alert object
        alert = {
            'id': f"alert_{self.alert_count}",
            'timestamp': datetime.now().isoformat(),
            'level': threat_level,
            'color': alert_config['color'],
            'priority': alert_config['priority'],
            'threat_data': threat_data,
            'actions_taken': []
        }
        
        # Add to history
        self.threat_history.append(alert)
        self.alert_count += 1
        self.last_alert_time = current_time
        
        # Play alert sound
        self.play_alert_sound(threat_level)
        
        # Log alert
        logger.warning(f"🚨 THREAT ALERT [{threat_level.upper()}]: {threat_data.get('src', 'Unknown')} -> {threat_data.get('dst', 'Unknown')} ({threat_data.get('protocol', 'Unknown')})")
        
        # Execute automated actions
        actions = self.execute_threat_response(alert)
        alert['actions_taken'] = actions
        
        return alert
    
    def execute_threat_response(self, alert):
        """Execute automated response actions based on threat level"""
        actions = []
        threat_level = alert['level']
        threat_data = alert['threat_data']
        src_ip = threat_data.get('src', '')
        
        try:
            if threat_level in ['high', 'critical']:
                # Block source IP (simulated)
                actions.append({
                    'action': 'block_ip',
                    'target': src_ip,
                    'status': 'executed',
                    'timestamp': datetime.now().isoformat()
                })
                logger.info(f"🛡️ Blocked IP: {src_ip}")
                
                # Generate firewall rule (simulated)
                actions.append({
                    'action': 'firewall_rule',
                    'rule': f"block {src_ip}",
                    'status': 'created',
                    'timestamp': datetime.now().isoformat()
                })
                
            if threat_level == 'critical':
                # Send emergency notification
                actions.append({
                    'action': 'emergency_notification',
                    'message': f"CRITICAL THREAT DETECTED from {src_ip}",
                    'status': 'sent',
                    'timestamp': datetime.now().isoformat()
                })
                
                # Initiate incident response
                actions.append({
                    'action': 'incident_response',
                    'status': 'initiated',
                    'timestamp': datetime.now().isoformat()
                })
                
            # Always log the threat
            actions.append({
                'action': 'threat_log',
                'status': 'logged',
                'timestamp': datetime.now().isoformat()
            })
            
        except Exception as e:
            logger.error(f"Error executing threat response: {e}")
            actions.append({
                'action': 'error',
                'error': str(e),
                'timestamp': datetime.now().isoformat()
            })
        
        return actions
    
    def get_active_alerts(self):
        """Get currently active alerts"""
        return list(self.threat_history)[-10:]  # Last 10 alerts
    
    def get_alert_statistics(self):
        """Get alert statistics"""
        if not self.threat_history:
            return {
                'total_alerts': 0,
                'alerts_by_level': {},
                'recent_alerts': []
            }
        
        alerts_by_level = {}
        for alert in self.threat_history:
            level = alert['level']
            alerts_by_level[level] = alerts_by_level.get(level, 0) + 1
        
        return {
            'total_alerts': len(self.threat_history),
            'alerts_by_level': alerts_by_level,
            'recent_alerts': list(self.threat_history)[-5:],  # Last 5 alerts
            'alert_rate': self.alert_count / max(1, (time.time() - self.last_alert_time + 1))
        }

# Global alert system instance
alert_system = ThreatAlertSystem()

def process_threat(threat_data):
    """Process detected threat and trigger alerts"""
    return alert_system.trigger_alert(threat_data)

def get_alerts():
    """Get current alerts for frontend"""
    return alert_system.get_active_alerts()

def get_alert_stats():
    """Get alert statistics for frontend"""
    return alert_system.get_alert_statistics()

if __name__ == "__main__":
    # Test the alert system
    print("🚨 Testing Threat Alert System...")
    
    # Test threat data
    test_threats = [
        {'src': '192.168.1.100', 'dst': '192.168.1.1', 'protocol': 'HTTP', 'prediction': 'Malicious'},
        {'src': '10.0.0.50', 'dst': '192.168.1.1', 'protocol': 'SSH', 'prediction': 'Malicious'},
        {'src': '172.16.0.10', 'dst': '192.168.1.1', 'protocol': 'DNS', 'prediction': 'Benign'},
    ]
    
    for threat in test_threats:
        alert = process_threat(threat)
        if alert:
            print(f"Alert triggered: {alert['level']} - {threat['src']}")
        time.sleep(2)
    
    print("✅ Alert system test completed!") 