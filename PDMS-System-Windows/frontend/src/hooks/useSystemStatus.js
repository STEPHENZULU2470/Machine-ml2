import { useState, useEffect } from 'react';
import { apiEndpoints } from '../utils/api';

export const useSystemStatus = () => {
  const [systemStatus, setSystemStatus] = useState(null);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState(null);

  const fetchSystemStatus = async () => {
    try {
      setIsLoading(true);
      setError(null);
      const response = await apiEndpoints.getSystemStatus();
      setSystemStatus(response.data);
    } catch (err) {
      setError(err.message);
      console.error('Failed to fetch system status:', err);
    } finally {
      setIsLoading(false);
    }
  };

  useEffect(() => {
    fetchSystemStatus();
    
    // Poll for updates every 5 seconds
    const interval = setInterval(fetchSystemStatus, 5000);
    
    return () => clearInterval(interval);
  }, []);

  return { systemStatus, isLoading, error, refetch: fetchSystemStatus };
};