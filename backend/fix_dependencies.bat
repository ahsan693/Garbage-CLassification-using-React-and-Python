@echo off
echo ============================================================
echo Fixing Flask and Werkzeug Compatibility Issues
echo ============================================================
echo.

set PYTHON_PATH=C:/Users/User/AppData/Local/Programs/Python/Python313/python.exe

echo Step 1: Uninstalling potentially incompatible packages...
"%PYTHON_PATH%" -m pip uninstall -y flask werkzeug flask-cors

echo.
echo Step 2: Installing exact compatible versions...
"%PYTHON_PATH%" -m pip install flask==2.0.1 werkzeug==2.0.1 flask-cors==3.0.10

echo.
echo Step 3: Verifying installed versions...
"%PYTHON_PATH%" -c "import flask; import werkzeug; from flask_cors import CORS; print(f'Flask version: {flask.__version__}'); print(f'Werkzeug version: {werkzeug.__version__}')"

echo.
echo If the above versions are Flask 2.0.1 and Werkzeug 2.0.1, the fix was successful.
echo.
echo Step 4: Attempting to run the Flask application...
"%PYTHON_PATH%" app.py

echo.
echo Press any key to exit...
pause > nul
