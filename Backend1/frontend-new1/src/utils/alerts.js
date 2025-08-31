// Alert sound utility
class AlertSystem {
  constructor() {
    this.audioContext = null;
    this.isInitialized = false;
  }

  async initialize() {
    if (this.isInitialized) return;
    
    try {
      // Initialize Web Audio API
      this.audioContext = new (window.AudioContext || window.webkitAudioContext)();
      this.isInitialized = true;
      console.log('Alert system initialized');
    } catch (error) {
      console.error('Failed to initialize alert system:', error);
    }
  }

  // Generate different alert sounds based on threat level
  async playAlert(threatLevel = 'medium') {
    await this.initialize();
    
    if (!this.audioContext) {
      console.warn('Audio context not available');
      return;
    }

    const oscillator = this.audioContext.createOscillator();
    const gainNode = this.audioContext.createGain();
    
    oscillator.connect(gainNode);
    gainNode.connect(this.audioContext.destination);
    
    // Different frequencies for different threat levels
    const frequencies = {
      low: [440, 554],      // A4, C#5
      medium: [659, 831],   // E5, G#5  
      high: [880, 1109],    // A5, C#6
      critical: [1318, 1661] // E6, G#6
    };
    
    const freqs = frequencies[threatLevel] || frequencies.medium;
    
    // Create alarm pattern
    const duration = threatLevel === 'critical' ? 2000 : 1000;
    const pulseCount = threatLevel === 'critical' ? 4 : 2;
    
    for (let i = 0; i < pulseCount; i++) {
      setTimeout(() => {
        const osc = this.audioContext.createOscillator();
        const gain = this.audioContext.createGain();
        
        osc.connect(gain);
        gain.connect(this.audioContext.destination);
        
        osc.frequency.setValueAtTime(freqs[0], this.audioContext.currentTime);
        osc.frequency.setValueAtTime(freqs[1], this.audioContext.currentTime + 0.1);
        osc.frequency.setValueAtTime(freqs[0], this.audioContext.currentTime + 0.2);
        
        gain.gain.setValueAtTime(0.3, this.audioContext.currentTime);
        gain.gain.exponentialRampToValueAtTime(0.01, this.audioContext.currentTime + 0.3);
        
        osc.start(this.audioContext.currentTime);
        osc.stop(this.audioContext.currentTime + 0.3);
      }, i * 400);
    }
  }

  // Play different sounds for different events
  async playUploadSuccess() {
    await this.initialize();
    if (!this.audioContext) return;

    const oscillator = this.audioContext.createOscillator();
    const gainNode = this.audioContext.createGain();
    
    oscillator.connect(gainNode);
    gainNode.connect(this.audioContext.destination);
    
    // Success sound: ascending notes
    oscillator.frequency.setValueAtTime(523, this.audioContext.currentTime); // C5
    oscillator.frequency.setValueAtTime(659, this.audioContext.currentTime + 0.1); // E5
    oscillator.frequency.setValueAtTime(784, this.audioContext.currentTime + 0.2); // G5
    
    gainNode.gain.setValueAtTime(0.2, this.audioContext.currentTime);
    gainNode.gain.exponentialRampToValueAtTime(0.01, this.audioContext.currentTime + 0.3);
    
    oscillator.start(this.audioContext.currentTime);
    oscillator.stop(this.audioContext.currentTime + 0.3);
  }

  async playError() {
    await this.initialize();
    if (!this.audioContext) return;

    const oscillator = this.audioContext.createOscillator();
    const gainNode = this.audioContext.createGain();
    
    oscillator.connect(gainNode);
    gainNode.connect(this.audioContext.destination);
    
    // Error sound: low descending notes
    oscillator.frequency.setValueAtTime(330, this.audioContext.currentTime); // E4
    oscillator.frequency.setValueAtTime(277, this.audioContext.currentTime + 0.15); // C#4
    oscillator.frequency.setValueAtTime(220, this.audioContext.currentTime + 0.3); // A3
    
    gainNode.gain.setValueAtTime(0.3, this.audioContext.currentTime);
    gainNode.gain.exponentialRampToValueAtTime(0.01, this.audioContext.currentTime + 0.45);
    
    oscillator.start(this.audioContext.currentTime);
    oscillator.stop(this.audioContext.currentTime + 0.45);
  }
}

export const alertSystem = new AlertSystem();

// Notification utility
export const showNotification = (message, type = 'info') => {
  // For browsers that support notifications
  if ('Notification' in window && Notification.permission === 'granted') {
    const notification = new Notification(`PDMS Alert`, {
      body: message,
      icon: '/favicon.ico',
      badge: '/favicon.ico',
      tag: 'pdms-alert'
    });
    
    setTimeout(() => notification.close(), 5000);
  }
};

// Request notification permission
export const requestNotificationPermission = async () => {
  if ('Notification' in window && Notification.permission === 'default') {
    await Notification.requestPermission();
  }
};