@echo off
setlocal
cd /d %~dp0

if "%1"=="status" (
    python dash.py
) else if "%1"=="run" (
    python src/main.py
) else if "%1"=="chat" (
    python src/agent.py
) else if "%1"=="sync" (
    git add .
    git commit -m "Auto-sync from mobile"
    git push origin main
) else (
    echo Vibe Coding Utility
    echo Usage: vibe [status^|run^|chat^|sync]
)
endlocal
