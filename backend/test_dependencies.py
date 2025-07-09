"""
Test script for PIL and Transformers integration
"""
import os
import sys

def test_pillow_installation():
    print("Testing PIL/Pillow installation...")
    try:
        from PIL import Image, __version__ as pil_version
        print(f"✅ PIL/Pillow {pil_version} is correctly installed")
        return True
    except ImportError as e:
        print(f"❌ PIL/Pillow import error: {e}")
        return False

def test_transformers_installation():
    print("\nTesting Transformers installation...")
    try:
        from transformers import __version__ as transformers_version
        print(f"✅ Transformers {transformers_version} is correctly installed")
        return True
    except ImportError as e:
        print(f"❌ Transformers import error: {e}")
        return False

def test_transformers_image_processing():
    print("\nTesting Transformers image processing capabilities...")
    try:
        from transformers import AutoImageProcessor
        print("✅ AutoImageProcessor imported successfully")
        return True
    except ImportError as e:
        print(f"❌ AutoImageProcessor import error: {e}")
        return False

def test_pipeline_with_sample():
    print("\nTesting image classification pipeline with a sample...")
    try:
        from transformers import pipeline
        print("Creating a simple image classification pipeline...")
        # Use a default model just for testing
        classifier = pipeline("image-classification")
        print("✅ Pipeline created successfully")
        
        # Try to create the specific pipeline (without downloading the full model)
        print("\nTesting initialization of our specific model pipeline...")
        try:
            classifier = pipeline("image-classification", model="yangy50/garbage-classification")
            print("✅ Specific model pipeline initialized successfully")
        except Exception as e:
            print(f"❌ Specific pipeline initialization error: {e}")
            print("This may require downloading the model and might take time.")
        
        return True
    except Exception as e:
        print(f"❌ Pipeline test error: {e}")
        return False

def check_python_paths():
    print("\nChecking Python paths...")
    import site
    print(f"Python executable: {sys.executable}")
    print(f"Python version: {sys.version}")
    print("\nPython path:")
    for p in sys.path:
        print(f"  - {p}")
    print("\nSite packages:")
    for p in site.getsitepackages():
        print(f"  - {p}")

def fix_pillow_if_needed():
    """Attempt to fix Pillow if it's not working"""
    try:
        from PIL import Image
        return True
    except ImportError:
        print("\n⚠️ PIL/Pillow not found, attempting to install...")
        import subprocess
        subprocess.check_call([sys.executable, "-m", "pip", "install", "--force-reinstall", "pillow==9.5.0"])
        try:
            from PIL import Image
            print("✅ PIL/Pillow successfully installed")
            return True
        except ImportError:
            print("❌ PIL/Pillow installation failed")
            return False

if __name__ == "__main__":
    print("=" * 60)
    print("PIL and Transformers Integration Test")
    print("=" * 60)
    
    # First check if Pillow is available or try to fix it
    if not test_pillow_installation():
        fix_pillow_if_needed()
    
    # Run all tests
    pillow_ok = test_pillow_installation()
    transformers_ok = test_transformers_installation()
    image_processing_ok = test_transformers_image_processing()
    pipeline_ok = test_pipeline_with_sample()
    
    # Show Python paths for debugging
    check_python_paths()
    
    print("\n" + "=" * 60)
    print("Test Results Summary")
    print("=" * 60)
    print(f"PIL/Pillow: {'✅ PASS' if pillow_ok else '❌ FAIL'}")
    print(f"Transformers: {'✅ PASS' if transformers_ok else '❌ FAIL'}")
    print(f"Image Processing: {'✅ PASS' if image_processing_ok else '❌ FAIL'}")
    print(f"Pipeline Test: {'✅ PASS' if pipeline_ok else '❌ FAIL'}")
    
    if all([pillow_ok, transformers_ok, image_processing_ok, pipeline_ok]):
        print("\n✅ All tests passed! You should be able to run the Flask app successfully.")
    else:
        print("\n❌ Some tests failed. Please address the issues before running the Flask app.")
    
    input("\nPress Enter to exit...")
