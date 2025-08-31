import axios from 'axios';

const API_BASE_URL = 'http://localhost:5000';

const api = axios.create({
  baseURL: API_BASE_URL,
  timeout: 30000,
  headers: {
    'Content-Type': 'application/json',
  },
});

// API endpoints
export const apiEndpoints = {
  // System status
  getSystemStatus: () => api.get('/system-status'),
  
  // File upload and prediction
  uploadFile: (formData) => api.post('/upload', formData, {
    headers: { 'Content-Type': 'multipart/form-data' }
  }),
  
  predict: (data) => api.post('/predict', { data }),
  predictUploaded: (formData) => api.post('/predict_uploaded', formData, {
    headers: { 'Content-Type': 'multipart/form-data' }
  }),
  predictUploadedSimple: (formData) => api.post('/predict_uploaded_simple', formData, {
    headers: { 'Content-Type': 'multipart/form-data' }
  }),
  
  // Model and metrics
  getMetrics: () => api.get('/metrics'),
  retrain: () => api.post('/retrain'),
  
  // Live predictions and history
  getLivePredictions: () => api.get('/live-predictions'),
  getHistory: () => api.get('/history'),
  
  // Threat management
  getAlerts: () => api.get('/alerts'),
  getAlertStats: () => api.get('/alert-stats'),
  testAlert: (data) => api.post('/test-alert', data),
  getThreatAnalysis: () => api.get('/threat-analysis'),
  
  // Actions
  blockIP: (data) => api.post('/block', data),
  reportThreat: (data) => api.post('/report', data),
  traceConnection: (data) => api.post('/trace', data),
  
  // Forensics
  getForensicLog: () => api.get('/forensic-log'),
  
  // Model comparison
  getModelComparison: () => api.get('/model-comparison'),
};

export default api;