import React, { useState, useRef } from 'react';
import { Upload, File, CheckCircle, AlertCircle, Loader } from 'lucide-react';
import { apiEndpoints } from '../utils/api';
import { alertSystem } from '../utils/alerts';
import toast from 'react-hot-toast';

const FileUpload = ({ onUploadSuccess }) => {
  const [isDragging, setIsDragging] = useState(false);
  const [uploadStatus, setUploadStatus] = useState('idle'); // idle, uploading, success, error
  const [selectedFile, setSelectedFile] = useState(null);
  const [predictionResults, setPredictionResults] = useState(null);
  const fileInputRef = useRef(null);

  const handleDragOver = (e) => {
    e.preventDefault();
    setIsDragging(true);
  };

  const handleDragLeave = (e) => {
    e.preventDefault();
    setIsDragging(false);
  };

  const handleDrop = (e) => {
    e.preventDefault();
    setIsDragging(false);
    
    const files = e.dataTransfer.files;
    if (files.length > 0) {
      handleFileSelect(files[0]);
    }
  };

  const handleFileSelect = (file) => {
    if (file && (file.type === 'text/csv' || file.name.endsWith('.csv'))) {
      setSelectedFile(file);
      setUploadStatus('idle');
      setPredictionResults(null);
    } else {
      toast.error('Please select a CSV file');
      alertSystem.playError();
    }
  };

  const handleFileInputChange = (e) => {
    if (e.target.files.length > 0) {
      handleFileSelect(e.target.files[0]);
    }
  };

  const uploadAndPredict = async () => {
    if (!selectedFile) {
      toast.error('Please select a file first');
      return;
    }

    setUploadStatus('uploading');
    
    try {
      const formData = new FormData();
      formData.append('file', selectedFile);

      // Upload and get predictions
      const response = await apiEndpoints.predictUploadedSimple(formData);
      
      setUploadStatus('success');
      setPredictionResults(response.data);
      
      // Play success sound
      await alertSystem.playUploadSuccess();
      toast.success(`File uploaded and analyzed! Found ${response.data.malicious_count || 0} threats`);
      
      if (onUploadSuccess) {
        onUploadSuccess(response.data);
      }
      
    } catch (error) {
      setUploadStatus('error');
      console.error('Upload failed:', error);
      toast.error(`Upload failed: ${error.response?.data?.error || error.message}`);
      await alertSystem.playError();
    }
  };

  const uploadForRetraining = async () => {
    if (!selectedFile) {
      toast.error('Please select a file first');
      return;
    }

    setUploadStatus('uploading');
    
    try {
      const formData = new FormData();
      formData.append('file', selectedFile);

      // Upload for retraining
      await apiEndpoints.uploadFile(formData);
      
      setUploadStatus('success');
      await alertSystem.playUploadSuccess();
      toast.success('File uploaded for retraining!');
      
      if (onUploadSuccess) {
        onUploadSuccess({ type: 'retrain' });
      }
      
    } catch (error) {
      setUploadStatus('error');
      console.error('Upload failed:', error);
      toast.error(`Upload failed: ${error.response?.data?.error || error.message}`);
      await alertSystem.playError();
    }
  };

  const getStatusIcon = () => {
    switch (uploadStatus) {
      case 'uploading':
        return <Loader className="animate-spin" />;
      case 'success':
        return <CheckCircle className="text-green-500" />;
      case 'error':
        return <AlertCircle className="text-red-500" />;
      default:
        return <Upload />;
    }
  };

  return (
    <div className="card">
      <h3 className="text-xl font-bold mb-4 text-gray-800">Dataset Upload & Analysis</h3>
      
      {/* File Upload Area */}
      <div
        className={`upload-area ${isDragging ? 'dragover' : ''}`}
        onDragOver={handleDragOver}
        onDragLeave={handleDragLeave}
        onDrop={handleDrop}
        onClick={() => fileInputRef.current?.click()}
      >
        <input
          ref={fileInputRef}
          type="file"
          accept=".csv"
          onChange={handleFileInputChange}
          style={{ display: 'none' }}
        />
        
        <div className="flex flex-col items-center gap-4">
          {getStatusIcon()}
          
          {selectedFile ? (
            <div className="text-center">
              <p className="font-semibold text-gray-700">{selectedFile.name}</p>
              <p className="text-sm text-gray-500">
                {(selectedFile.size / 1024 / 1024).toFixed(2)} MB
              </p>
            </div>
          ) : (
            <div className="text-center">
              <p className="font-semibold text-gray-700">
                Drop your CSV file here or click to browse
              </p>
              <p className="text-sm text-gray-500">
                Supports any dataset format for threat analysis
              </p>
            </div>
          )}
        </div>
      </div>

      {/* Action Buttons */}
      {selectedFile && (
        <div className="flex gap-3 mt-4">
          <button
            onClick={uploadAndPredict}
            disabled={uploadStatus === 'uploading'}
            className="btn btn-primary flex items-center gap-2"
          >
            <File size={16} />
            Analyze for Threats
          </button>
          
          <button
            onClick={uploadForRetraining}
            disabled={uploadStatus === 'uploading'}
            className="btn btn-success flex items-center gap-2"
          >
            <Upload size={16} />
            Upload for Retraining
          </button>
        </div>
      )}

      {/* Prediction Results */}
      {predictionResults && (
        <div className="mt-6 p-4 bg-gray-50 rounded-lg">
          <h4 className="font-bold text-gray-800 mb-2">Analysis Results:</h4>
          <div className="grid grid-cols-2 gap-4">
            <div className="text-center">
              <div className="text-2xl font-bold text-green-600">
                {predictionResults.benign_count || 0}
              </div>
              <div className="text-sm text-gray-600">Benign</div>
            </div>
            <div className="text-center">
              <div className="text-2xl font-bold text-red-600">
                {predictionResults.malicious_count || 0}
              </div>
              <div className="text-sm text-gray-600">Threats</div>
            </div>
          </div>
          
          {predictionResults.malicious_count > 0 && (
            <div className="mt-4 p-3 bg-red-100 border border-red-300 rounded-lg">
              <p className="text-red-800 font-semibold">
                ⚠️ {predictionResults.malicious_count} potential threats detected!
              </p>
            </div>
          )}
        </div>
      )}
    </div>
  );
};

export default FileUpload;