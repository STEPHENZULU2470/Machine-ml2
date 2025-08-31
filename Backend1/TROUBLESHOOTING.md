# Troubleshooting Guide

## Common Issues and Solutions

### 1. Python Import Errors

**Problem**: `ModuleNotFoundError: No module named 'flask'`
**Solution**: 
```bash
# Activate virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 2. File Encoding Issues

**Problem**: `SyntaxError: source code string cannot contain null bytes`
**Solution**: 
- Files with UTF-16 BOM or Windows line endings have been fixed
- All Python files now use UTF-8 encoding with Unix line endings

### 3. Missing Dependencies

**Problem**: `No module named 'requests'`
**Solution**: 
```bash
source venv/bin/activate
pip install requests
```

### 4. Packet Capture Issues

**Problem**: `TShark not found` or packet capture not working
**Solution**: 
```bash
# Install tshark (Wireshark command-line tools)
sudo apt install tshark

# Or on other systems:
# macOS: brew install wireshark
# Windows: Download from https://www.wireshark.org/
```

### 5. Model Loading Issues

**Problem**: `Model files not found`
**Solution**: 
```bash
# Train the initial model
python3 train_model.py

# Or use the startup script
./start.sh
```

### 6. Dataset Path Issues

**Problem**: `Dataset not found`
**Solution**: 
- Ensure your dataset CSV files are in the correct location
- Check the relative paths in the scripts
- Use absolute paths if needed

### 7. Permission Issues

**Problem**: `Permission denied` when creating directories or files
**Solution**: 
```bash
# Check current permissions
ls -la

# Fix permissions if needed
chmod 755 .
chmod 644 *.py
```

### 8. Port Already in Use

**Problem**: `Address already in use`
**Solution**: 
```bash
# Find process using port 5000
lsof -i :5000

# Kill the process
kill -9 <PID>

# Or use a different port
export FLASK_RUN_PORT=5001
python3 app.py
```

### 9. Virtual Environment Issues

**Problem**: `venv/bin/activate: No such file or directory`
**Solution**: 
```bash
# Recreate virtual environment
rm -rf venv
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 10. Memory Issues

**Problem**: `MemoryError` when loading large datasets
**Solution**: 
- Use smaller datasets for testing
- Increase system memory
- Use chunked processing for large files

## System Requirements

- **Python**: 3.8 or higher
- **Memory**: At least 4GB RAM recommended
- **Storage**: At least 2GB free space
- **Network**: Internet access for package installation

## Supported Operating Systems

- **Linux**: Ubuntu 18.04+, Debian 10+, CentOS 7+
- **macOS**: 10.14+ (Mojave or later)
- **Windows**: 10 or later (with WSL recommended)

## Getting Help

1. Check this troubleshooting guide first
2. Review the error messages in the console
3. Check the Flask application logs
4. Ensure all dependencies are installed
5. Verify file paths and permissions

## Quick Fix Commands

```bash
# Complete reset and setup
rm -rf venv
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
mkdir -p dataset uploads
python3 train_model.py
python3 app.py
```