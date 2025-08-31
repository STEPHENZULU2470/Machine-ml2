import React, { useState, useEffect } from 'react';
import { motion } from 'framer-motion';
import { Toaster } from 'react-hot-toast';
import { Shield, Upload, Activity, Settings, Brain } from 'lucide-react';

import Dashboard from './components/Dashboard';
import FileUpload from './components/FileUpload';
import ThreatActions from './components/ThreatActions';
import ModelStatus from './components/ModelStatus';

import { useSystemStatus } from './hooks/useSystemStatus';
import { useLiveAlerts } from './hooks/useLiveAlerts';
import { requestNotificationPermission } from './utils/alerts';

function App() {
  const [activeTab, setActiveTab] = useState('dashboard');
  const { systemStatus, isLoading: statusLoading, error: statusError, refetch: refetchStatus } = useSystemStatus();
  const { alerts, alertStats, livePredictions, testAlert } = useLiveAlerts();
  const [metrics, setMetrics] = useState(null);

  // Request notification permission on load
  useEffect(() => {
    requestNotificationPermission();
  }, []);

  // Fetch metrics
  useEffect(() => {
    const fetchMetrics = async () => {
      try {
        const { apiEndpoints } = await import('./utils/api');
        const response = await apiEndpoints.getMetrics();
        setMetrics(response.data);
      } catch (error) {
        console.error('Failed to fetch metrics:', error);
      }
    };

    fetchMetrics();
    const interval = setInterval(fetchMetrics, 10000); // Every 10 seconds
    return () => clearInterval(interval);
  }, []);

  const tabs = [
    { id: 'dashboard', label: 'Dashboard', icon: Activity },
    { id: 'upload', label: 'Upload Dataset', icon: Upload },
    { id: 'actions', label: 'Threat Actions', icon: Shield },
    { id: 'model', label: 'Model Status', icon: Brain },
  ];

  const handleUploadSuccess = (result) => {
    // Refresh system status and metrics after upload
    refetchStatus();
    
    // If threats were detected, trigger test alert
    if (result.malicious_count > 0) {
      testAlert('high');
    }
  };

  const handleActionComplete = (action, data) => {
    console.log(`Action completed: ${action}`, data);
    refetchStatus();
  };

  const handleRetrainComplete = (newMetrics) => {
    setMetrics(newMetrics);
    refetchStatus();
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-500 via-purple-600 to-purple-800">
      <div className="container">
        {/* Header */}
        <motion.div 
          initial={{ y: -20, opacity: 0 }}
          animate={{ y: 0, opacity: 1 }}
          className="card mb-6"
        >
          <div className="flex items-center justify-between">
            <div className="flex items-center gap-3">
              <Shield className="text-blue-600" size={40} />
              <div>
                <h1 className="text-3xl font-bold text-gray-800">
                  PDMS
                </h1>
                <p className="text-gray-600">
                  AI-Powered Intrusion Detection & Mitigation System
                </p>
              </div>
            </div>
            
            {statusLoading ? (
              <div className="loading"></div>
            ) : statusError ? (
              <div className="text-red-600 font-semibold">Connection Error</div>
            ) : (
              <div className="flex items-center gap-2">
                <div className={`status-indicator ${systemStatus?.status === 'operational' ? 'status-online' : 'status-offline'}`}></div>
                <span className="font-semibold text-gray-700">
                  {systemStatus?.status?.toUpperCase() || 'UNKNOWN'}
                </span>
              </div>
            )}
          </div>
        </motion.div>

        {/* Navigation Tabs */}
        <motion.div 
          initial={{ y: -10, opacity: 0 }}
          animate={{ y: 0, opacity: 1 }}
          transition={{ delay: 0.1 }}
          className="card mb-6"
        >
          <div className="flex space-x-1">
            {tabs.map((tab) => {
              const Icon = tab.icon;
              return (
                <button
                  key={tab.id}
                  onClick={() => setActiveTab(tab.id)}
                  className={`flex items-center gap-2 px-4 py-2 rounded-lg font-medium transition-all ${
                    activeTab === tab.id
                      ? 'bg-blue-600 text-white shadow-lg'
                      : 'text-gray-600 hover:bg-gray-100'
                  }`}
                >
                  <Icon size={18} />
                  {tab.label}
                </button>
              );
            })}
          </div>
        </motion.div>

        {/* Tab Content */}
        <motion.div
          key={activeTab}
          initial={{ x: 20, opacity: 0 }}
          animate={{ x: 0, opacity: 1 }}
          transition={{ duration: 0.3 }}
        >
          {activeTab === 'dashboard' && (
            <Dashboard 
              systemStatus={systemStatus}
              alerts={alerts}
              alertStats={alertStats}
              livePredictions={livePredictions}
            />
          )}
          
          {activeTab === 'upload' && (
            <FileUpload onUploadSuccess={handleUploadSuccess} />
          )}
          
          {activeTab === 'actions' && (
            <ThreatActions onActionComplete={handleActionComplete} />
          )}
          
          {activeTab === 'model' && (
            <ModelStatus 
              metrics={metrics}
              onRetrainComplete={handleRetrainComplete}
            />
          )}
        </motion.div>
      </div>

      {/* Toast Notifications */}
      <Toaster
        position="top-right"
        toastOptions={{
          duration: 4000,
          style: {
            background: 'rgba(255, 255, 255, 0.95)',
            backdropFilter: 'blur(10px)',
            border: '1px solid rgba(255, 255, 255, 0.2)',
            borderRadius: '12px',
          },
        }}
      />
    </div>
  );
}

export default App;