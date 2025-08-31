import React, { useState } from 'react';
import { Shield, Ban, Flag, Search, Volume2 } from 'lucide-react';
import { apiEndpoints } from '../utils/api';
import { alertSystem } from '../utils/alerts';
import toast from 'react-hot-toast';

const ThreatActions = ({ onActionComplete }) => {
  const [isLoading, setIsLoading] = useState(false);
  const [ipAddress, setIpAddress] = useState('');
  const [protocol, setProtocol] = useState('');

  const handleBlock = async () => {
    if (!ipAddress) {
      toast.error('Please enter an IP address');
      return;
    }

    setIsLoading(true);
    try {
      await apiEndpoints.blockIP({ 
        src_ip: ipAddress, 
        protocol: protocol || 'TCP' 
      });
      
      toast.success(`Successfully blocked ${ipAddress}`);
      await alertSystem.playUploadSuccess();
      
      if (onActionComplete) {
        onActionComplete('block', { ip: ipAddress, protocol });
      }
      
      setIpAddress('');
      setProtocol('');
    } catch (error) {
      toast.error(`Failed to block IP: ${error.response?.data?.error || error.message}`);
      await alertSystem.playError();
    } finally {
      setIsLoading(false);
    }
  };

  const handleReport = async () => {
    if (!ipAddress) {
      toast.error('Please enter an IP address');
      return;
    }

    setIsLoading(true);
    try {
      await apiEndpoints.reportThreat({ 
        src_ip: ipAddress, 
        protocol: protocol || 'TCP' 
      });
      
      toast.success(`Successfully reported ${ipAddress}`);
      await alertSystem.playUploadSuccess();
      
      if (onActionComplete) {
        onActionComplete('report', { ip: ipAddress, protocol });
      }
    } catch (error) {
      toast.error(`Failed to report threat: ${error.response?.data?.error || error.message}`);
      await alertSystem.playError();
    } finally {
      setIsLoading(false);
    }
  };

  const handleTrace = async () => {
    if (!ipAddress) {
      toast.error('Please enter an IP address');
      return;
    }

    setIsLoading(true);
    try {
      const response = await apiEndpoints.traceConnection({ 
        src_ip: ipAddress, 
        protocol: protocol || 'TCP' 
      });
      
      toast.success(`Trace initiated for ${ipAddress}`);
      console.log('Trace results:', response.data);
      
      if (onActionComplete) {
        onActionComplete('trace', { ip: ipAddress, protocol, results: response.data });
      }
    } catch (error) {
      toast.error(`Failed to trace connection: ${error.response?.data?.error || error.message}`);
      await alertSystem.playError();
    } finally {
      setIsLoading(false);
    }
  };

  const testAlertSounds = async () => {
    toast.success('Testing alert sounds...');
    
    // Test different alert levels
    setTimeout(() => alertSystem.playAlert('low'), 100);
    setTimeout(() => alertSystem.playAlert('medium'), 1500);
    setTimeout(() => alertSystem.playAlert('high'), 3000);
    setTimeout(() => alertSystem.playAlert('critical'), 4500);
  };

  return (
    <div className="card">
      <div className="flex items-center gap-2 mb-4">
        <Shield className="text-blue-600" size={24} />
        <h3 className="text-lg font-bold text-gray-800">Threat Response Actions</h3>
      </div>

      {/* IP Address Input */}
      <div className="space-y-4">
        <div>
          <label className="block text-sm font-medium text-gray-700 mb-2">
            IP Address
          </label>
          <input
            type="text"
            value={ipAddress}
            onChange={(e) => setIpAddress(e.target.value)}
            placeholder="e.g., 192.168.1.100"
            className="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
          />
        </div>

        <div>
          <label className="block text-sm font-medium text-gray-700 mb-2">
            Protocol (Optional)
          </label>
          <select
            value={protocol}
            onChange={(e) => setProtocol(e.target.value)}
            className="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
          >
            <option value="">Auto-detect</option>
            <option value="TCP">TCP</option>
            <option value="UDP">UDP</option>
            <option value="ICMP">ICMP</option>
          </select>
        </div>

        {/* Action Buttons */}
        <div className="grid grid-cols-3 gap-3">
          <button
            onClick={handleBlock}
            disabled={isLoading || !ipAddress}
            className="btn btn-danger flex items-center justify-center gap-2"
          >
            <Ban size={16} />
            Block
          </button>
          
          <button
            onClick={handleReport}
            disabled={isLoading || !ipAddress}
            className="btn btn-primary flex items-center justify-center gap-2"
          >
            <Flag size={16} />
            Report
          </button>
          
          <button
            onClick={handleTrace}
            disabled={isLoading || !ipAddress}
            className="btn btn-success flex items-center justify-center gap-2"
          >
            <Search size={16} />
            Trace
          </button>
        </div>

        {/* Test Alert Sounds */}
        <div className="pt-4 border-t border-gray-200">
          <button
            onClick={testAlertSounds}
            className="btn btn-primary flex items-center justify-center gap-2 w-full"
          >
            <Volume2 size={16} />
            Test Alert Sounds
          </button>
          <p className="text-xs text-gray-500 mt-2 text-center">
            Tests all alert sound levels: Low → Medium → High → Critical
          </p>
        </div>
      </div>
    </div>
  );
};

export default ThreatActions;