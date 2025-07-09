@echo off
echo Starting Garbage Classification Backend Server with compatible dependencies...
echo.

set PYTHON_PATH=C:/Users/User/AppData/Local/Programs/Python/Python313/python.exe

echo Using Python at: %PYTHON_PATH%
echo Starting Flask server...
echo.

"%PYTHON_PATH%" -c "import flask; import werkzeug; print(f'Flask version: {flask.__version__}'); print(f'Werkzeug version: {werkzeug.__version__}')"
echo.
echo If versions are compatible (Flask 2.0.1 and Werkzeug 2.0.1), starting the server...
"%PYTHON_PATH%" app.py

if %ERRORLEVEL% NEQ 0 (
    echo.
    echo Server stopped with exit code %ERRORLEVEL%
    echo Press any key to exit...
    pause > nul
)
