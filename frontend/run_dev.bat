@echo off
title Python Quest Frontend Dev Server
cd /d "%~dp0"

echo ========================================================
echo        STARTING PYTHON QUEST FRONTEND (DEV MODE)
echo ========================================================
echo.

where node >nul 2>nul
if errorlevel 1 (
    echo [ERROR] Node.js is required. Please install Node.js 18+ from https://nodejs.org/
    pause
    exit /b 1
)

if not exist "node_modules\vite" (
    echo [Setup] First time setup: Installing npm dependencies...
    echo (This only happens once and may take 1-2 minutes)
    echo.
    call npm install
    if errorlevel 1 (
        echo.
        echo [ERROR] Failed to install npm dependencies.
        echo Please ensure you are connected to the internet and try running 'npm install' manually.
        pause
        exit /b 1
    )
)

echo.
echo Starting Vite development server...
echo.
call npm run dev
pause
