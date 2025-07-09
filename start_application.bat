@echo off
echo ============================================================
echo Starting Garbage Classification Application Setup
echo ============================================================

echo.
echo Setting up Backend...
cd /d "%~dp0backend"

REM Fix backend dependencies
echo.
echo Installing specific backend dependencies...
pip uninstall -y pillow flask flask-cors werkzeug
pip install pillow==9.5.0 flask==2.0.1 flask-cors==3.0.10 werkzeug==2.0.1 torchvision==0.15.1

if not exist venv (
    echo Creating Python virtual environment...
    python -m venv venv
)

echo Activating virtual environment...
call venv\Scripts\activate

echo Installing Python dependencies...
pip install -r requirements.txt

echo.
echo Setting up Frontend...
cd /d "%~dp0garbage-classification"

echo.
echo Installing specific React dependencies...
call npm install react-router-dom axios --save

echo.
echo Starting both servers...
echo.

echo Starting Flask server in a new window...
start cmd /k "cd /d "%~dp0backend" && python app.py"

echo Starting React development server in a new window...
start cmd /k "cd /d "%~dp0garbage-classification" && npm start"

echo.
echo ============================================================
echo Setup complete! The application should open in your browser shortly.
echo If it doesn't open automatically, visit: http://localhost:3000
echo ============================================================
echo.
echo Press any key to exit...
pause > nul
