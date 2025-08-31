# 🌐 PDMS Frontend - React Dashboard

Modern, responsive web interface for the PDMS Intrusion Detection System with real-time monitoring, file upload, and audio alerts.

## 🚀 Quick Start

```bash
# Install dependencies
npm install

# Start development server
npm run dev
```

Frontend runs on: **http://localhost:3000**

## 🎯 Features

### 📁 **File Upload Interface**
- **Drag & drop** CSV file upload
- **Real-time progress** indicators
- **Instant analysis** results
- **Support for any dataset** format

### 🔊 **Audio Alert System**
- **Web Audio API** for rich sound generation
- **4 threat levels** with unique sounds:
  - 🟢 **Low**: Gentle notification beep
  - 🟡 **Medium**: Standard alarm tone
  - 🟠 **High**: Urgent alarm sequence
  - 🔴 **Critical**: Continuous urgent alarm
- **Success sounds** for completed actions
- **Error sounds** for failed operations

### 📊 **Real-time Dashboard**
- **Live system metrics** with auto-refresh
- **Threat statistics** visualization
- **System health** monitoring
- **Active alerts** management
- **Circular progress** indicators

### 🛡️ **Threat Management**
- **IP blocking** interface
- **Threat reporting** system
- **Network tracing** tools
- **Manual threat** response actions

## 🛠️ Technical Stack

### Core Technologies
- **React 18** - Modern UI framework
- **Vite** - Fast build tool and dev server
- **Axios** - HTTP client for API calls
- **Framer Motion** - Smooth animations

### UI Components
- **Lucide React** - Beautiful icons
- **React Hot Toast** - Elegant notifications
- **React Circular Progressbar** - Metrics visualization
- **Custom CSS** - Glassmorphism design

### State Management
- **React Hooks** - useState, useEffect
- **Custom hooks** - useSystemStatus, useLiveAlerts
- **Real-time polling** - Auto-refresh data

## 📱 User Interface

### Navigation Tabs
1. **📊 Dashboard** - System overview and live monitoring
2. **📁 Upload Dataset** - File upload and analysis
3. **🛡️ Threat Actions** - Response and management tools
4. **🧠 Model Status** - ML model performance and management

### Design Features
- **Glassmorphism** styling with blur effects
- **Responsive design** for all screen sizes
- **Smooth animations** for better UX
- **Color-coded alerts** for quick recognition
- **Professional gradient** backgrounds

## 🔊 Audio System Implementation

### Web Audio API Features
```javascript
// Different frequencies for threat levels
const frequencies = {
  low: [440, 554],      // A4, C#5
  medium: [659, 831],   // E5, G#5  
  high: [880, 1109],    // A5, C#6
  critical: [1318, 1661] // E6, G#6
};
```

### Sound Types
- **Threat alerts** - Based on severity level
- **Upload success** - Ascending musical notes
- **Error notifications** - Descending warning tones
- **Action confirmations** - Success chimes

## 🔗 Backend Integration

### API Communication
- **Axios interceptors** for error handling
- **Real-time polling** every 2-5 seconds
- **Automatic retries** for failed requests
- **CORS support** for cross-origin requests

### Data Flow
1. **Frontend** sends requests to backend API
2. **Backend** processes data and returns results
3. **Frontend** updates UI and plays audio alerts
4. **Real-time polling** keeps data synchronized

## 📊 Dashboard Components

### System Status
- **Real-time health** monitoring
- **Uptime tracking** and system metrics
- **Connection status** indicators
- **Performance statistics**

### Threat Visualization
- **Active alerts** with severity levels
- **Live predictions** stream
- **Threat statistics** with charts
- **Historical data** analysis

### File Upload
- **Drag & drop** area with visual feedback
- **File validation** and error handling
- **Progress tracking** during upload
- **Results display** with threat counts

## 🎨 Styling & Themes

### Color Scheme
- **Primary**: Blue gradient (#667eea → #764ba2)
- **Success**: Green (#2ed573)
- **Warning**: Yellow/Orange (#ffa726)
- **Danger**: Red (#ff6b6b)
- **Background**: Purple gradient

### Responsive Design
- **Mobile-first** approach
- **Flexible grid** layouts
- **Adaptive components** for different screen sizes
- **Touch-friendly** interface elements

## 🔧 Development

### Available Scripts
- `npm run dev` - Start development server
- `npm run build` - Build for production
- `npm run preview` - Preview production build

### Development Features
- **Hot reload** for instant updates
- **Error overlay** for debugging
- **Source maps** for easier debugging
- **Fast refresh** preserves component state

## 🌐 Deployment

### Production Build
```bash
npm run build
# Serve the dist/ folder with any web server
```

### Environment Configuration
- **API_BASE_URL** - Backend server URL
- **Development proxy** - Auto-configured in Vite
- **CORS handling** - Configured in backend

## 🔍 Browser Support

- **Chrome/Edge** 88+ (recommended)
- **Firefox** 85+
- **Safari** 14+
- **Web Audio API** support required for alerts

## 🎉 Ready to Use!

Your frontend is now fully integrated with:
- ✅ **Real-time backend** communication
- ✅ **Audio alert system** for threats
- ✅ **File upload** for any dataset
- ✅ **Beautiful, responsive** interface
- ✅ **Professional dashboard** with metrics

Start the development server and begin monitoring your network! 🛡️