@echo off
title Storyboard Engine v10.3
echo.
echo  ================================
echo   STORYBOARD ENGINE v10.3
echo   Starting up... please wait
echo  ================================
echo.

:: Check if Python exists
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo  ERROR: Python is not installed!
    echo.
    echo  1. Go to https://python.org
    echo  2. Download and install Python
    echo  3. IMPORTANT: Check "Add Python to PATH" during install
    echo  4. Restart your computer
    echo  5. Double-click this file again
    echo.
    pause
    exit /b 1
)

:: Install dependencies if needed
echo  Installing dependencies...
pip install -r requirements.txt >nul 2>&1
pip install pywebview >nul 2>&1
echo  Done!
echo.

:: Launch the app
echo  Opening the engine...
echo  (Close this window to stop the app)
echo.
python desktop.py
pause
