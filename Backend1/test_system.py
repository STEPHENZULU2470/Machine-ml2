#!/usr/bin/env python3
"""
System Test Script for IDS Backend
Tests all major components and reports status
"""

import os
import sys
import importlib

def test_imports():
    """Test if all required modules can be imported"""
    print("🔍 Testing module imports...")
    
    required_modules = [
        'flask', 'flask_cors', 'pandas', 'sklearn', 'shap', 
        'pyshark', 'numpy', 'matplotlib', 'seaborn', 'joblib', 
        'werkzeug', 'requests'
    ]
    
    failed_imports = []
    for module in required_modules:
        try:
            importlib.import_module(module)
            print(f"  ✅ {module}")
        except ImportError as e:
            print(f"  ❌ {module}: {e}")
            failed_imports.append(module)
    
    if failed_imports:
        print(f"\n⚠️  {len(failed_imports)} modules failed to import")
        return False
    else:
        print("✅ All required modules imported successfully")
        return True

def test_files():
    """Test if all required files exist"""
    print("\n📁 Testing file structure...")
    
    required_files = [
        'app.py', 'requirements.txt', 'features.txt', 
        'rf_model.joblib', 'shap_explainer.joblib'
    ]
    
    missing_files = []
    for file in required_files:
        if os.path.exists(file):
            size = os.path.getsize(file)
            print(f"  ✅ {file} ({size:,} bytes)")
        else:
            print(f"  ❌ {file} (missing)")
            missing_files.append(file)
    
    if missing_files:
        print(f"\n⚠️  {len(missing_files)} files are missing")
        return False
    else:
        print("✅ All required files present")
        return True

def test_directories():
    """Test if required directories exist"""
    print("\n📂 Testing directory structure...")
    
    required_dirs = ['dataset', 'uploads', 'venv']
    
    missing_dirs = []
    for dir_name in required_dirs:
        if os.path.exists(dir_name):
            print(f"  ✅ {dir_name}/")
        else:
            print(f"  ❌ {dir_name}/ (missing)")
            missing_dirs.append(dir_name)
    
    if missing_dirs:
        print(f"\n⚠️  {len(missing_dirs)} directories are missing")
        return False
    else:
        print("✅ All required directories present")
        return True

def test_python_syntax():
    """Test if all Python files have valid syntax"""
    print("\n🐍 Testing Python syntax...")
    
    python_files = [f for f in os.listdir('.') if f.endswith('.py')]
    syntax_errors = []
    
    for py_file in python_files:
        try:
            with open(py_file, 'r') as f:
                compile(f.read(), py_file, 'exec')
            print(f"  ✅ {py_file}")
        except SyntaxError as e:
            print(f"  ❌ {py_file}: {e}")
            syntax_errors.append(py_file)
    
    if syntax_errors:
        print(f"\n⚠️  {len(syntax_errors)} Python files have syntax errors")
        return False
    else:
        print("✅ All Python files have valid syntax")
        return True

def test_model_files():
    """Test if model files can be loaded"""
    print("\n🤖 Testing model files...")
    
    try:
        import joblib
        
        # Test loading the model
        if os.path.exists('rf_model.joblib'):
            model = joblib.load('rf_model.joblib')
            print(f"  ✅ rf_model.joblib loaded (type: {type(model).__name__})")
        else:
            print("  ❌ rf_model.joblib not found")
            return False
            
        # Test loading the explainer
        if os.path.exists('shap_explainer.joblib'):
            explainer = joblib.load('shap_explainer.joblib')
            print(f"  ✅ shap_explainer.joblib loaded (type: {type(explainer).__name__})")
        else:
            print("  ❌ shap_explainer.joblib not found")
            return False
            
        # Test loading features
        if os.path.exists('features.txt'):
            with open('features.txt', 'r') as f:
                features = [line.strip() for line in f if line.strip()]
            print(f"  ✅ features.txt loaded ({len(features)} features)")
        else:
            print("  ❌ features.txt not found")
            return False
            
        return True
        
    except Exception as e:
        print(f"  ❌ Error loading model files: {e}")
        return False

def test_system_requirements():
    """Test system requirements"""
    print("\n💻 Testing system requirements...")
    
    # Check Python version
    python_version = sys.version_info
    if python_version.major >= 3 and python_version.minor >= 8:
        print(f"  ✅ Python {python_version.major}.{python_version.minor}.{python_version.micro}")
    else:
        print(f"  ❌ Python {python_version.major}.{python_version.minor}.{python_version.micro} (3.8+ required)")
        return False
    
    # Check available memory (rough estimate)
    try:
        import psutil
        memory = psutil.virtual_memory()
        memory_gb = memory.total / (1024**3)
        if memory_gb >= 2:
            print(f"  ✅ Memory: {memory_gb:.1f} GB")
        else:
            print(f"  ⚠️  Memory: {memory_gb:.1f} GB (2+ GB recommended)")
    except ImportError:
        print("  ⚠️  psutil not available, cannot check memory")
    
    # Check disk space
    try:
        disk_usage = os.statvfs('.')
        free_gb = (disk_usage.f_frsize * disk_usage.f_bavail) / (1024**3)
        if free_gb >= 1:
            print(f"  ✅ Disk space: {free_gb:.1f} GB free")
        else:
            print(f"  ⚠️  Disk space: {free_gb:.1f} GB free (1+ GB recommended)")
    except Exception as e:
        print(f"  ⚠️  Cannot check disk space: {e}")
    
    return True

def main():
    """Run all tests"""
    print("🚀 IDS Backend System Test")
    print("=" * 50)
    
    tests = [
        ("Module Imports", test_imports),
        ("File Structure", test_files),
        ("Directory Structure", test_directories),
        ("Python Syntax", test_python_syntax),
        ("Model Files", test_model_files),
        ("System Requirements", test_system_requirements)
    ]
    
    results = []
    for test_name, test_func in tests:
        try:
            result = test_func()
            results.append((test_name, result))
        except Exception as e:
            print(f"  ❌ {test_name} failed with error: {e}")
            results.append((test_name, False))
    
    # Summary
    print("\n" + "=" * 50)
    print("📊 TEST SUMMARY")
    print("=" * 50)
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for test_name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{status} {test_name}")
    
    print(f"\nOverall: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! The system is ready to use.")
        print("\nTo start the system:")
        print("  source venv/bin/activate")
        print("  python3 app.py")
        print("\nOr use the startup script:")
        print("  ./start.sh")
    else:
        print("⚠️  Some tests failed. Please check the issues above.")
        print("\nFor help, see TROUBLESHOOTING.md")
        
        # Suggest fixes
        if not os.path.exists('venv'):
            print("\n💡 Try: python3 -m venv venv")
        if not os.path.exists('rf_model.joblib'):
            print("💡 Try: python3 train_model.py")
    
    return passed == total

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)