import React, { useState } from 'react';
import { Brain, RefreshCw, BarChart3, Target } from 'lucide-react';
import { apiEndpoints } from '../utils/api';
import { alertSystem } from '../utils/alerts';
import toast from 'react-hot-toast';

const ModelStatus = ({ metrics, onRetrainComplete }) => {
  const [isRetraining, setIsRetraining] = useState(false);
  const [modelComparison, setModelComparison] = useState(null);

  const handleRetrain = async () => {
    setIsRetraining(true);
    
    try {
      await apiEndpoints.retrain();
      toast.success('Model retraining started! This may take a few minutes...');
      await alertSystem.playUploadSuccess();
      
      // Poll for completion (simplified - in production you'd use websockets)
      setTimeout(async () => {
        try {
          const newMetrics = await apiEndpoints.getMetrics();
          if (onRetrainComplete) {
            onRetrainComplete(newMetrics.data);
          }
          toast.success('Model retraining completed!');
        } catch (error) {
          console.error('Failed to get updated metrics:', error);
        }
        setIsRetraining(false);
      }, 30000); // 30 seconds
      
    } catch (error) {
      setIsRetraining(false);
      toast.error(`Retraining failed: ${error.response?.data?.error || error.message}`);
      await alertSystem.playError();
    }
  };

  const loadModelComparison = async () => {
    try {
      const response = await apiEndpoints.getModelComparison();
      setModelComparison(response.data);
      toast.success('Model comparison loaded');
    } catch (error) {
      toast.error(`Failed to load model comparison: ${error.response?.data?.error || error.message}`);
    }
  };

  const formatMetricValue = (value) => {
    if (value === null || value === undefined) return 'N/A';
    if (typeof value === 'number') return (value * 100).toFixed(2) + '%';
    return value;
  };

  return (
    <div className="space-y-6">
      {/* Model Metrics */}
      <div className="card">
        <div className="flex items-center justify-between mb-4">
          <div className="flex items-center gap-2">
            <Brain className="text-purple-600" size={24} />
            <h3 className="text-lg font-bold text-gray-800">Model Performance</h3>
          </div>
          
          <button
            onClick={handleRetrain}
            disabled={isRetraining}
            className="btn btn-primary flex items-center gap-2"
          >
            <RefreshCw className={isRetraining ? 'animate-spin' : ''} size={16} />
            {isRetraining ? 'Retraining...' : 'Retrain Model'}
          </button>
        </div>

        <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
          <div className="metric-card">
            <div className="metric-value text-green-600">
              {formatMetricValue(metrics?.accuracy)}
            </div>
            <div className="metric-label">Accuracy</div>
          </div>
          
          <div className="metric-card">
            <div className="metric-value text-blue-600">
              {formatMetricValue(metrics?.precision)}
            </div>
            <div className="metric-label">Precision</div>
          </div>
          
          <div className="metric-card">
            <div className="metric-value text-orange-600">
              {formatMetricValue(metrics?.recall)}
            </div>
            <div className="metric-label">Recall</div>
          </div>
          
          <div className="metric-card">
            <div className="metric-value text-purple-600">
              {formatMetricValue(metrics?.f1_score)}
            </div>
            <div className="metric-label">F1 Score</div>
          </div>
        </div>
      </div>

      {/* Model Comparison */}
      <div className="card">
        <div className="flex items-center justify-between mb-4">
          <div className="flex items-center gap-2">
            <BarChart3 className="text-green-600" size={24} />
            <h3 className="text-lg font-bold text-gray-800">Model Comparison</h3>
          </div>
          
          <button
            onClick={loadModelComparison}
            className="btn btn-success flex items-center gap-2"
          >
            <Target size={16} />
            Load Comparison
          </button>
        </div>

        {modelComparison ? (
          <div className="space-y-4">
            <div className="text-sm text-gray-600 mb-2">
              Comparison of different ML models for intrusion detection:
            </div>
            
            <div className="overflow-x-auto">
              <table className="w-full text-sm">
                <thead>
                  <tr className="border-b border-gray-200">
                    <th className="text-left py-2 px-3">Model</th>
                    <th className="text-left py-2 px-3">Accuracy</th>
                    <th className="text-left py-2 px-3">Precision</th>
                    <th className="text-left py-2 px-3">Recall</th>
                    <th className="text-left py-2 px-3">F1 Score</th>
                  </tr>
                </thead>
                <tbody>
                  {modelComparison.models?.map((model, index) => (
                    <tr key={index} className="border-b border-gray-100">
                      <td className="py-2 px-3 font-semibold">{model.name}</td>
                      <td className="py-2 px-3">{formatMetricValue(model.accuracy)}</td>
                      <td className="py-2 px-3">{formatMetricValue(model.precision)}</td>
                      <td className="py-2 px-3">{formatMetricValue(model.recall)}</td>
                      <td className="py-2 px-3">{formatMetricValue(model.f1_score)}</td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          </div>
        ) : (
          <div className="text-center py-8 text-gray-500">
            Click "Load Comparison" to see model performance comparison
          </div>
        )}
      </div>
    </div>
  );
};

export default ModelStatus;