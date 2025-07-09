@echo off
echo Starting Garbage Classification Backend Server...
echo.

set PYTHON_PATH=C:/Users/User/AppData/Local/Programs/Python/Python313/python.exe

echo Using Python at: %PYTHON_PATH%
echo Starting Flask server...
echo.

"%PYTHON_PATH%" app.py

if %ERRORLEVEL% NEQ 0 (
    echo.
    echo Server stopped with exit code %ERRORLEVEL%
    echo Press any key to exit...
    pause > nul
)
