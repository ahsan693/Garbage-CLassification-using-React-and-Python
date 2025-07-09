import sys
import os
import importlib.metadata

def check_environment():
    """Check the Python environment for required packages and versions."""
    required_packages = {
        'flask': '2.0.1',
        'werkzeug': '2.0.1',
        'flask-cors': '3.0.10',
    }
    
    print(f"Python version: {sys.version}")
    print("Checking required packages:")
    
    all_compatible = True
    for package, version in required_packages.items():
        try:
            installed_version = importlib.metadata.version(package)
            if installed_version != version:
                print(f"⚠️ {package}: installed={installed_version}, required={version}")
                all_compatible = False
            else:
                print(f"✓ {package}: {installed_version}")
        except importlib.metadata.PackageNotFoundError:
            print(f"❌ {package}: Not installed")
            all_compatible = False
    
    if not all_compatible:
        print("\nWarning: Some package versions are not compatible!")
        print("Consider reinstalling the exact versions specified in requirements.txt:")
        print("pip uninstall -y flask werkzeug flask-cors")
        print("pip install -r requirements.txt")
    
    return all_compatible

if __name__ == "__main__":
    print("=" * 50)
    print("Garbage Classification Backend - Environment Check")
    print("=" * 50)
    
    check_environment()
    
    print("\nAttempting to run the Flask application...")
    try:
        # Import after checking to see any import errors
        from app import app
        app.run(host='0.0.0.0', port=5000, debug=True)
    except Exception as e:
        print(f"\nError running Flask app: {str(e)}")
        import traceback
        traceback.print_exc()
        print("\nPlease fix the issues above and try again.")
        
    print("\nPress Enter to exit...")
    input()
