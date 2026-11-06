@echo off
title Python Quest Launcher
echo ========================================================
echo             STARTING PYTHON QUEST APPLICATION
echo ========================================================
echo.

cd /d "%~dp0"

where node >nul 2>nul
if errorlevel 1 (
    echo [ERROR] Node.js is required to run the development site.
    echo Install Node.js 18 or newer, then run this file again.
    pause
    exit /b 1
)

set "PYTHON_EXE="
for /d %%P in ("%LOCALAPPDATA%\Programs\Python\Python*") do (
    if exist "%%~fP\python.exe" set "PYTHON_EXE=%%~fP\python.exe"
)
if defined PYTHON_EXE (
    "%PYTHON_EXE%" --version >nul 2>nul
    if errorlevel 1 set "PYTHON_EXE="
)
if not defined PYTHON_EXE (
    for /f "delims=" %%P in ('where python 2^>nul') do (
        "%%P" --version >nul 2>nul
        if not errorlevel 1 if not defined PYTHON_EXE set "PYTHON_EXE=%%P"
    )
)
if not defined PYTHON_EXE (
    echo [ERROR] Python 3.10 or newer was not found.
    echo Install Python from python.org, enable Add Python to PATH, and run this file again.
    pause
    exit /b 1
)

if not exist "%~dp0backend\.venv\Scripts\python.exe" (
    echo Creating the backend Python environment...
    "%PYTHON_EXE%" -m venv "%~dp0backend\.venv"
    if errorlevel 1 (
        echo [ERROR] Could not create the backend Python environment.
        pause
        exit /b 1
    )
)

"%~dp0backend\.venv\Scripts\python.exe" -c "import flask, flask_cors, sqlalchemy" >nul 2>nul
if errorlevel 1 (
    echo Installing backend packages from requirements.txt. This may take a few minutes the first time...
    "%~dp0backend\.venv\Scripts\python.exe" -m pip install -r "%~dp0backend\requirements.txt"
    if errorlevel 1 (
        echo [ERROR] Backend package installation failed. Check your internet connection and try again.
        pause
        exit /b 1
    )
)

if not exist "%~dp0frontend\node_modules\vite" (
    echo Installing frontend packages. This may take a minute or two the first time...
    cd /d "%~dp0frontend"
    call npm install
    if errorlevel 1 (
        echo [ERROR] Frontend package installation failed. Check your internet connection and try again.
        pause
        exit /b 1
    )
    cd /d "%~dp0"
)

echo [1/3] Starting Python Backend Server on Port 5000...
start "Python Quest Backend" /D "%~dp0backend" cmd /k ""%~dp0backend\.venv\Scripts\python.exe" run.py"

timeout /t 2 /nobreak >nul

echo [2/3] Starting Frontend Server on Port 5173...
start "Python Quest Frontend" /D "%~dp0frontend" cmd /k "set ""PYTHON_EXECUTABLE=%~dp0backend\.venv\Scripts\python.exe"" && npm run dev"

timeout /t 3 /nobreak >nul

echo [3/3] Opening Python Quest in your Web Browser...
start http://localhost:5173/

echo.
echo ========================================================
echo  Python Quest is now running!
echo  URL: http://localhost:5173/
echo ========================================================
echo  Keep the two opened command windows running while using the app.
echo  To exit, simply close those two command windows.
echo.
pause
