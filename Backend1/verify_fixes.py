#!/usr/bin/env python3
"""
Verification script to test all the fixes applied to the codebase.
"""

import sys
import importlib
import traceback

def test_imports():
    """Test that all required modules can be imported"""
    print("🔍 Testing imports...")
    
    modules_to_test = [
        'flask',
        'flask_cors', 
        'pandas',
        'sklearn',
        'shap',
        'pyshark',
        'numpy',
        'matplotlib',
        'seaborn',
        'joblib',
        'werkzeug',
        'requests'
    ]
    
    failed_imports = []
    
    for module in modules_to_test:
        try:
            importlib.import_module(module)
            print(f"  ✅ {module}")
        except ImportError as e:
            print(f"  ❌ {module}: {e}")
            failed_imports.append(module)
    
    return len(failed_imports) == 0, failed_imports

def test_model_loading():
    """Test that model files can be loaded"""
    print("\n🤖 Testing model loading...")
    
    try:
        import joblib
        
        # Test model loading
        model = joblib.load('rf_model.joblib')
        print(f"  ✅ Model loaded: {type(model)}")
        
        # Test explainer loading  
        explainer = joblib.load('shap_explainer.joblib')
        print(f"  ✅ Explainer loaded: {type(explainer)}")
        
        # Test features loading
        with open('features.txt', 'r') as f:
            features = [line.strip() for line in f.readlines()]
        print(f"  ✅ Features loaded: {len(features)} features")
        
        return True
        
    except Exception as e:
        print(f"  ❌ Model loading failed: {e}")
        return False

def test_python_syntax():
    """Test that all Python files have valid syntax"""
    print("\n📝 Testing Python syntax...")
    
    import glob
    import py_compile
    import tempfile
    import os
    
    python_files = glob.glob('*.py')
    failed_files = []
    
    for file in python_files:
        try:
            # Use py_compile to check syntax
            with tempfile.NamedTemporaryFile(suffix='.pyc', delete=True) as tmp:
                py_compile.compile(file, tmp.name, doraise=True)
            print(f"  ✅ {file}")
        except py_compile.PyCompileError as e:
            print(f"  ❌ {file}: {e}")
            failed_files.append(file)
        except Exception as e:
            print(f"  ❌ {file}: {e}")
            failed_files.append(file)
    
    return len(failed_files) == 0, failed_files

def test_app_initialization():
    """Test that the Flask app can be initialized"""
    print("\n🌐 Testing Flask app initialization...")
    
    try:
        # Import the app module
        import app
        print("  ✅ App module imported successfully")
        
        # Check if Flask app is created
        if hasattr(app, 'app'):
            print("  ✅ Flask app instance created")
            
            # Test basic route
            with app.app.test_client() as client:
                response = client.get('/')
                if response.status_code == 200:
                    print("  ✅ Basic route works")
                    return True
                else:
                    print(f"  ❌ Basic route failed: {response.status_code}")
                    return False
        else:
            print("  ❌ Flask app instance not found")
            return False
            
    except Exception as e:
        print(f"  ❌ App initialization failed: {e}")
        traceback.print_exc()
        return False

def main():
    """Run all verification tests"""
    print("🚀 Starting verification of fixes...\n")
    
    all_passed = True
    
    # Test imports
    imports_ok, failed_imports = test_imports()
    if not imports_ok:
        print(f"❌ Import test failed: {failed_imports}")
        all_passed = False
    
    # Test model loading
    models_ok = test_model_loading()
    if not models_ok:
        print("❌ Model loading test failed")
        all_passed = False
    
    # Test Python syntax
    syntax_ok, failed_files = test_python_syntax()
    if not syntax_ok:
        print(f"❌ Syntax test failed: {failed_files}")
        all_passed = False
    
    # Test app initialization
    app_ok = test_app_initialization()
    if not app_ok:
        print("❌ App initialization test failed")
        all_passed = False
    
    print("\n" + "="*50)
    if all_passed:
        print("🎉 ALL TESTS PASSED! The codebase is working correctly.")
        return 0
    else:
        print("❌ Some tests failed. Please check the errors above.")
        return 1

if __name__ == '__main__':
    sys.exit(main())