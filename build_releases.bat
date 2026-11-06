@echo off
title Python Quest Release Builder
echo ========================================================
echo        BUILDING PYTHON QUEST RELEASES (EXE & APK)
echo ========================================================
echo.

cd /d "%~dp0"

echo [1/4] Building Frontend Production Assets...
cd /d "%~dp0frontend"
if not exist "%~dp0frontend\node_modules\vite" (
    echo Installing frontend packages...
    call npm install
    if errorlevel 1 (
        echo [ERROR] Frontend package installation failed. Check Node.js and your internet connection.
        pause
        exit /b 1
    )
)
call npm run build
if %ERRORLEVEL% neq 0 (
    echo [ERROR] Frontend build failed!
    pause
    exit /b %ERRORLEVEL%
)

echo.
echo [2/4] Building Windows Desktop EXE with PyInstaller...
cd /d "%~dp0"
python -m PyInstaller python_quest.spec --clean --noconfirm
if %ERRORLEVEL% neq 0 (
    echo [ERROR] Windows EXE build failed!
    pause
    exit /b %ERRORLEVEL%
)

echo Packaging Windows Desktop Application into ZIP...
powershell -Command "Compress-Archive -Path '%~dp0dist\PythonQuest' -DestinationPath '%~dp0PythonQuest-Windows-x64.zip' -Force"

echo.
echo [3/4] Syncing Capacitor & Building Android APK...
cd /d "%~dp0frontend"
call npx cap sync android
if %ERRORLEVEL% neq 0 (
    echo [WARNING] Capacitor sync warning.
)

set JAVA_HOME=C:\Program Files\Android\Android Studio\jbr
set PATH=%JAVA_HOME%\bin;%PATH%
set ANDROID_HOME=%LOCALAPPDATA%\Android\Sdk
set ANDROID_SDK_ROOT=%ANDROID_HOME%
set ANDROID_USER_HOME=%~dp0temp\android-user-home
if not exist "%ANDROID_USER_HOME%" mkdir "%ANDROID_USER_HOME%"
cd /d "%~dp0frontend\android"
call .\gradlew.bat assembleDebug
if %ERRORLEVEL% equ 0 (
    copy /Y "%~dp0frontend\android\app\build\outputs\apk\debug\app-debug.apk" "%~dp0python-quest.apk" >nul
    echo [+] Fresh python-quest.apk created in root folder!
) else (
    echo [!] Android APK build skipped or failed (check JDK/Android SDK).
)

echo.
echo ========================================================
echo  BUILD COMPLETE!
echo.
echo  1. Windows PC Application:
echo     Folder: %~dp0dist\PythonQuest\PythonQuest.exe
echo     Zip:    %~dp0PythonQuest-Windows-x64.zip
echo.
echo  2. Android Mobile Application:
echo     APK:    %~dp0python-quest.apk
echo ========================================================
pause
