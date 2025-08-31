import React from 'react';
import { Shield, Activity, AlertTriangle, CheckCircle, Clock, Target } from 'lucide-react';
import { CircularProgressbar, buildStyles } from 'react-circular-progressbar';
import 'react-circular-progressbar/dist/styles.css';

const Dashboard = ({ systemStatus, alerts, alertStats, livePredictions }) => {
  const getStatusColor = (status) => {
    switch (status) {
      case 'operational': return 'text-green-600';
      case 'warning': return 'text-yellow-600';
      case 'critical': return 'text-red-600';
      default: return 'text-gray-600';
    }
  };

  const getUptimeString = (uptime) => {
    if (!uptime) return 'Unknown';
    const hours = Math.floor(uptime / 3600);
    const minutes = Math.floor((uptime % 3600) / 60);
    return `${hours}h ${minutes}m`;
  };

  const getThreatRate = () => {
    if (!systemStatus) return 0;
    const total = systemStatus.total_packets_analyzed || 1;
    const threats = systemStatus.threats_detected || 0;
    return Math.round((threats / total) * 100);
  };

  return (
    <div className="space-y-6">
      {/* System Status Header */}
      <div className="card">
        <div className="flex items-center justify-between">
          <div className="flex items-center gap-3">
            <Shield className="text-blue-600" size={32} />
            <div>
              <h2 className="text-2xl font-bold text-gray-800">
                PDMS - Intrusion Detection System
              </h2>
              <div className="flex items-center gap-2 mt-1">
                <div className={`status-indicator ${systemStatus?.status === 'operational' ? 'status-online' : 'status-offline'}`}></div>
                <span className={`font-semibold ${getStatusColor(systemStatus?.status)}`}>
                  {systemStatus?.status?.toUpperCase() || 'UNKNOWN'}
                </span>
              </div>
            </div>
          </div>
          
          <div className="text-right">
            <div className="text-sm text-gray-600">Uptime</div>
            <div className="font-semibold text-gray-800">
              {getUptimeString(systemStatus?.uptime)}
            </div>
          </div>
        </div>
      </div>

      {/* Metrics Grid */}
      <div className="metrics-grid">
        <div className="metric-card">
          <div className="metric-value text-blue-600">
            {systemStatus?.total_packets_analyzed || 0}
          </div>
          <div className="metric-label">Packets Analyzed</div>
        </div>
        
        <div className="metric-card">
          <div className="metric-value text-red-600">
            {systemStatus?.threats_detected || 0}
          </div>
          <div className="metric-label">Threats Detected</div>
        </div>
        
        <div className="metric-card">
          <div className="metric-value text-yellow-600">
            {systemStatus?.false_positives || 0}
          </div>
          <div className="metric-label">False Positives</div>
        </div>
        
        <div className="metric-card">
          <div style={{ width: 80, height: 80, margin: '0 auto' }}>
            <CircularProgressbar
              value={getThreatRate()}
              text={`${getThreatRate()}%`}
              styles={buildStyles({
                textColor: '#667eea',
                pathColor: getThreatRate() > 10 ? '#ff6b6b' : '#667eea',
                trailColor: '#e0e7ff'
              })}
            />
          </div>
          <div className="metric-label mt-2">Threat Rate</div>
        </div>
      </div>

      {/* Active Alerts */}
      {alerts && alerts.length > 0 && (
        <div className="card alert-card">
          <div className="flex items-center gap-2 mb-4">
            <AlertTriangle className="text-red-600" size={24} />
            <h3 className="text-lg font-bold text-red-800">Active Threats</h3>
          </div>
          
          <div className="space-y-3">
            {alerts.slice(0, 5).map((alert, index) => (
              <div key={index} className="flex items-center justify-between p-3 bg-white rounded-lg border border-red-200">
                <div className="flex items-center gap-3">
                  <div className={`w-3 h-3 rounded-full ${
                    alert.level === 'critical' ? 'bg-red-600' :
                    alert.level === 'high' ? 'bg-orange-500' :
                    alert.level === 'medium' ? 'bg-yellow-500' : 'bg-blue-500'
                  }`}></div>
                  <div>
                    <div className="font-semibold text-gray-800">
                      {alert.level?.toUpperCase()} threat from {alert.src_ip}
                    </div>
                    <div className="text-sm text-gray-600">
                      {alert.timestamp} • Actions: {alert.actions_taken?.length || 0}
                    </div>
                  </div>
                </div>
                
                <div className="flex gap-2">
                  <span className={`px-2 py-1 rounded text-xs font-semibold ${
                    alert.level === 'critical' ? 'bg-red-100 text-red-800' :
                    alert.level === 'high' ? 'bg-orange-100 text-orange-800' :
                    alert.level === 'medium' ? 'bg-yellow-100 text-yellow-800' :
                    'bg-blue-100 text-blue-800'
                  }`}>
                    {alert.level}
                  </span>
                </div>
              </div>
            ))}
          </div>
        </div>
      )}

      {/* Live Predictions Stream */}
      {livePredictions && livePredictions.length > 0 && (
        <div className="card">
          <div className="flex items-center gap-2 mb-4">
            <Activity className="text-blue-600" size={24} />
            <h3 className="text-lg font-bold text-gray-800">Live Traffic Analysis</h3>
          </div>
          
          <div className="log-container">
            {livePredictions.slice(-10).map((prediction, index) => (
              <div key={index} className={`mb-1 ${
                prediction.prediction === 'malicious' ? 'threat-high' : 'benign'
              }`}>
                [{prediction.timestamp}] {prediction.src} → {prediction.dst} | 
                {prediction.protocol} | {prediction.prediction?.toUpperCase()}
              </div>
            ))}
          </div>
        </div>
      )}

      {/* System Health */}
      {systemStatus?.system_health && (
        <div className="card">
          <div className="flex items-center gap-2 mb-4">
            <CheckCircle className="text-green-600" size={24} />
            <h3 className="text-lg font-bold text-gray-800">System Health</h3>
          </div>
          
          <div className="grid grid-cols-2 gap-4">
            <div className="p-3 bg-gray-50 rounded-lg">
              <div className="text-sm text-gray-600">CPU Usage</div>
              <div className="text-lg font-semibold text-gray-800">
                {systemStatus.system_health.cpu_usage || 'N/A'}%
              </div>
            </div>
            
            <div className="p-3 bg-gray-50 rounded-lg">
              <div className="text-sm text-gray-600">Memory Usage</div>
              <div className="text-lg font-semibold text-gray-800">
                {systemStatus.system_health.memory_usage || 'N/A'}%
              </div>
            </div>
            
            <div className="p-3 bg-gray-50 rounded-lg">
              <div className="text-sm text-gray-600">Network Interfaces</div>
              <div className="text-lg font-semibold text-gray-800">
                {systemStatus.system_health.network_interfaces || 'N/A'}
              </div>
            </div>
            
            <div className="p-3 bg-gray-50 rounded-lg">
              <div className="text-sm text-gray-600">Model Status</div>
              <div className="text-lg font-semibold text-green-600">
                {systemStatus.system_health.model_loaded ? 'Loaded' : 'Not Loaded'}
              </div>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};

export default Dashboard;