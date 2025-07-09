@echo off
echo ============================================================
echo Fixing Dependencies for Garbage Classification Backend
echo ============================================================
echo.

set PYTHON_PATH=C:/Users/User/AppData/Local/Programs/Python/Python313/python.exe

echo Step 1: Uninstalling potentially problematic packages...
"%PYTHON_PATH%" -m pip uninstall -y pillow

echo.
echo Step 2: Installing required packages with specific versions...
"%PYTHON_PATH%" -m pip install pillow==9.5.0
"%PYTHON_PATH%" -m pip install torchvision

echo.
echo Step 3: Verifying PIL/Pillow installation...
"%PYTHON_PATH%" -c "from PIL import Image; from PIL import __version__ as pil_version; print(f'PIL/Pillow version: {pil_version}'); print('PIL/Pillow is correctly installed!')"

if %ERRORLEVEL% NEQ 0 (
    echo ERROR: PIL/Pillow verification failed!
    echo.
    echo Attempting to install Pillow via alternative method...
    "%PYTHON_PATH%" -m pip install --force-reinstall pillow==9.5.0
    echo.
    echo Verifying again...
    "%PYTHON_PATH%" -c "from PIL import Image; print('PIL/Pillow is now correctly installed!')"
)

echo.
echo Step 4: Testing transformers with image processing...
"%PYTHON_PATH%" -c "from transformers import AutoImageProcessor; print('AutoImageProcessor imported successfully!'); from PIL import Image; print('PIL works with transformers!')"

echo.
echo Step 5: Running the Flask application...
"%PYTHON_PATH%" app.py

if %ERRORLEVEL% NEQ 0 (
    echo.
    echo Application failed to start. Press any key to exit...
    pause > nul
)
