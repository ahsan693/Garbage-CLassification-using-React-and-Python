Write-Host "Starting Garbage Classification Backend Server..." -ForegroundColor Green

# Get the Python executable path
$PythonPath = "C:/Users/User/AppData/Local/Programs/Python/Python313/python.exe"

Write-Host "Using Python at: $PythonPath" -ForegroundColor Cyan
Write-Host "Starting Flask server..." -ForegroundColor Yellow

# Run the Flask application
& $PythonPath app.py

# Keep the window open if there's an error
if ($LASTEXITCODE -ne 0) {
    Write-Host "Server stopped with exit code $LASTEXITCODE" -ForegroundColor Red
    Write-Host "Press any key to exit..." -ForegroundColor Gray
    $null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
}
