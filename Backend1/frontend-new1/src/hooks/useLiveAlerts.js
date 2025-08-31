import { useState, useEffect } from 'react';
import { apiEndpoints } from '../utils/api';
import { alertSystem, showNotification } from '../utils/alerts';

export const useLiveAlerts = () => {
  const [alerts, setAlerts] = useState([]);
  const [alertStats, setAlertStats] = useState(null);
  const [livePredictions, setLivePredictions] = useState([]);

  const fetchAlerts = async () => {
    try {
      const [alertsRes, statsRes, predictionsRes] = await Promise.all([
        apiEndpoints.getAlerts(),
        apiEndpoints.getAlertStats(),
        apiEndpoints.getLivePredictions()
      ]);
      
      const newAlerts = alertsRes.data.alerts || [];
      const newPredictions = predictionsRes.data.live_predictions || [];
      
      // Check for new threats and play alerts
      if (newAlerts.length > alerts.length) {
        const latestAlert = newAlerts[newAlerts.length - 1];
        if (latestAlert && latestAlert.level) {
          await alertSystem.playAlert(latestAlert.level);
          showNotification(
            `${latestAlert.level.toUpperCase()} threat detected from ${latestAlert.src_ip}`,
            'warning'
          );
        }
      }
      
      // Check for new malicious predictions
      if (newPredictions.length > livePredictions.length) {
        const newMalicious = newPredictions.filter(p => 
          p.prediction === 'malicious' && 
          !livePredictions.some(old => old.timestamp === p.timestamp)
        );
        
        if (newMalicious.length > 0) {
          await alertSystem.playAlert('medium');
          showNotification(
            `${newMalicious.length} new malicious packet(s) detected`,
            'warning'
          );
        }
      }
      
      setAlerts(newAlerts);
      setAlertStats(statsRes.data);
      setLivePredictions(newPredictions);
      
    } catch (error) {
      console.error('Failed to fetch alerts:', error);
    }
  };

  useEffect(() => {
    fetchAlerts();
    
    // Poll for new alerts every 2 seconds
    const interval = setInterval(fetchAlerts, 2000);
    
    return () => clearInterval(interval);
  }, [alerts.length, livePredictions.length]);

  const testAlert = async (threatLevel = 'medium') => {
    try {
      await apiEndpoints.testAlert({ threat_level: threatLevel });
      await alertSystem.playAlert(threatLevel);
      showNotification(`Test ${threatLevel} alert triggered`, 'info');
    } catch (error) {
      console.error('Failed to test alert:', error);
    }
  };

  return {
    alerts,
    alertStats,
    livePredictions,
    testAlert,
    refetch: fetchAlerts
  };
};